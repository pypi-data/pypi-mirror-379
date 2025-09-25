"""Code to build cost layer file"""

import json
import logging
from warnings import warn

import dask.config
import dask.distributed
from gaps.cli import CLICommandFromFunction

from revrt.models.cost_layers import ALL, TransmissionLayerCreationConfig
from revrt.costs.layer_creator import LayerCreator
from revrt.costs.dry_costs_creator import DryCostsCreator
from revrt.costs.masks import Masks
from revrt.utilities import (
    LayeredFile,
    load_data_using_layer_file_profile,
    save_data_using_layer_file_profile,
)
from revrt.exceptions import revrtAttributeError, revrtConfigurationError
from revrt.warn import revrtWarning


logger = logging.getLogger(__name__)
CONFIG_ACTIONS = ["layers", "dry_costs", "merge_friction_and_barriers"]


def build_routing_layers(  # noqa: PLR0917, PLR0913
    routing_file,
    template_file=None,
    input_layer_dir=".",
    output_tiff_dir=".",
    masks_dir=".",
    layers=None,
    dry_costs=None,
    merge_friction_and_barriers=None,
    max_workers=1,
    memory_limit_per_worker="auto",
    create_kwargs=None,
):
    """Create costs, barriers, and frictions from a config file

    You can re-run this function on an existing file to add new layers
    without overwriting existing layers or needing to change your
    original config.

    Parameters
    ----------
    routing_file : path-like
        Path to GeoTIFF/Zarr file to store cost layers in. If the file
        does not exist, it will be created based on the `template_file`
        input.
    template_file : path-like, optional
        Path to template GeoTIFF (``*.tif`` or ``*.tiff``) or Zarr
        (``*.zarr``) file containing the profile and transform to be
        used for the layered costs file. If ``None``, then the
        `routing_file`  is assumed to exist on disk already.
        By default, ``None``.
    input_layer_dir : path-like, optional
        Directory to search for input layers in, if not found in
        current directory. By default, ``'.'``.
    output_tiff_dir : path-like, optional
        Directory where cost layers should be saved as GeoTIFF.
        By default, ``"."``.
    masks_dir : path-like, optional
        Directory for storing/finding mask GeoTIFFs (wet, dry, landfall,
        wet+, dry+). By default, ``"."``.
    layers : list of LayerConfig, optional
        Configuration for layers to be built and added to the file.
        At least one of `layers`, `dry_costs`, or
        `merge_friction_and_barriers` must be defined.
        By default, ``None``.
    dry_costs : DryCosts, optional
        Configuration for dry cost layers to be built and added to the
        file. At least one of `layers`, `dry_costs`, or
        `merge_friction_and_barriers` must be defined.
        By default, ``None``.
    merge_friction_and_barriers : MergeFrictionBarriers, optional
        Configuration for merging friction and barriers and adding to
        the layered costs file. At least one of `layers`, `dry_costs`,
        or `merge_friction_and_barriers` must be defined.
        By default, ``None``
    max_workers : int, optional
        Number of parallel workers to use for file creation. If ``None``
        or >1, processing is performed in parallel using Dask.
        By default, ``1``.
    memory_limit_per_worker : str, float, int, or None, default="auto"
        Sets the memory limit *per worker*. This only applies if
        ``max_workers != 1``. If ``None`` or ``0``, no limit is applied.
        If ``"auto"``, the total system memory is split evenly between
        the workers. If a float, that fraction of the system memory is
        used *per worker*. If a string giving a number  of bytes (like
        "1GiB"), that amount is used *per worker*. If an int, that
        number of bytes is used *per worker*. By default, ``"auto"``
    create_kwargs : dict, optional
        Additional keyword arguments to pass to
        :meth:`LayeredFile.create_new` when creating a new layered file.
        Do not include ``template_file``; it will be ignored.
        By default, ``None``.
    """
    config = _validated_config(
        routing_file=routing_file,
        template_file=template_file or routing_file,
        input_layer_dir=input_layer_dir,
        output_tiff_dir=output_tiff_dir,
        masks_dir=masks_dir,
        layers=layers,
        dry_costs=dry_costs,
        merge_friction_and_barriers=merge_friction_and_barriers,
    )
    logger.debug(
        "Using dask config:\n%s", json.dumps(dask.config.config, indent=4)
    )

    lock = None
    if max_workers != 1:
        client = dask.distributed.Client(
            n_workers=max_workers, memory_limit=memory_limit_per_worker
        )
        logger.info(
            "Dask client created with %s workers and %r memory limit per "
            "worker",
            max_workers,
            memory_limit_per_worker,
        )
        logger.info("Dashboard link: %s", client.dashboard_link)
        lock = dask.distributed.Lock("rioxarray-write", client=client)

    lf_handler = LayeredFile(fp=config.routing_file)
    if not lf_handler.fp.exists():
        create_kwargs = create_kwargs or {}
        create_kwargs.pop("template_file", None)
        logger.info(
            "%s not found. Creating new layered file with kwargs:\n%r",
            lf_handler.fp,
            create_kwargs,
        )
        lf_handler.create_new(
            template_file=config.template_file, **create_kwargs
        )

    masks = _load_masks(config, lf_handler)

    builder = LayerCreator(
        lf_handler,
        masks,
        input_layer_dir=config.input_layer_dir,
        output_tiff_dir=config.output_tiff_dir,
    )
    _build_layers(config, builder, lf_handler, lock=lock)

    if config.dry_costs is not None:
        _build_dry_costs(config, masks, lf_handler, lock=lock)

    if config.merge_friction_and_barriers is not None:
        _combine_friction_and_barriers(config, lf_handler, lock=lock)


def _validated_config(**config_dict):
    """Validate use config inputs"""
    config = TransmissionLayerCreationConfig.model_validate(config_dict)
    if not any(config.model_dump()[key] is not None for key in CONFIG_ACTIONS):
        msg = f"At least one of {CONFIG_ACTIONS!r} must be in the config file"
        raise revrtConfigurationError(msg)

    return config


def _load_masks(config, lf_handler):
    """Load masks based on config file"""
    masks = Masks(
        shape=lf_handler.shape,
        crs=lf_handler.profile["crs"],
        transform=lf_handler.profile["transform"],
        masks_dir=config.masks_dir,
    )
    if not config.layers:
        return masks

    build_configs = [lc.build for lc in config.layers]
    need_masks = any(
        lc.extent != ALL for bc in build_configs for lc in bc.values()
    )
    if need_masks:
        masks.load(lf_handler.fp)

    return masks


def _build_layers(config, builder, lf_handler, lock):
    """Build layers from config file"""
    existing_layers = set(lf_handler.data_layers)

    for lc in config.layers or []:
        if lc.layer_name in existing_layers:
            logger.info(
                "Layer %r already exists in %s! Skipping...",
                lc.layer_name,
                lf_handler.fp,
            )
            continue

        builder.build(
            lc.layer_name,
            lc.build,
            values_are_costs_per_mile=lc.values_are_costs_per_mile,
            write_to_file=lc.include_in_file,
            description=lc.description,
            lock=lock,
        )


def _build_dry_costs(config, masks, lf_handler, lock):
    """Build dry costs from config file"""
    dc = config.dry_costs

    dry_mask = None
    try:
        dry_mask = masks.dry_mask
    except revrtAttributeError:
        msg = "Dry mask not found! Computing dry costs for full extent!"
        warn(msg, revrtWarning)

    dcc = DryCostsCreator(
        lf_handler,
        input_layer_dir=config.input_layer_dir,
        output_tiff_dir=config.output_tiff_dir,
    )
    cost_configs = None if not dc.cost_configs else str(dc.cost_configs)
    dcc.build(
        iso_region_tiff=dc.iso_region_tiff,
        nlcd_tiff=dc.nlcd_tiff,
        slope_tiff=dc.slope_tiff,
        transmission_config=cost_configs,
        mask=dry_mask,
        default_mults=dc.default_mults,
        extra_tiffs=dc.extra_tiffs,
        lock=lock,
    )


def _combine_friction_and_barriers(config, io_handler, lock):
    """Combine friction and barriers and save to layered file"""

    logger.info("Loading friction and raw barriers")

    merge_config = config.merge_friction_and_barriers
    friction = load_data_using_layer_file_profile(
        io_handler.fp,
        f"{merge_config.friction_layer}.tif",
        layer_dirs=[config.output_tiff_dir, config.input_layer_dir],
    )
    barriers = load_data_using_layer_file_profile(
        io_handler.fp,
        f"{merge_config.barrier_layer}.tif",
        layer_dirs=[config.output_tiff_dir, config.input_layer_dir],
    )
    combined = friction + barriers * merge_config.barrier_multiplier

    out_fp = config.output_tiff_dir / f"{merge_config.output_layer_name}.tif"
    logger.debug("Saving combined barriers to %s", out_fp)
    save_data_using_layer_file_profile(
        layer_fp=io_handler.fp, data=combined, geotiff=out_fp, lock=lock
    )

    logger.info("Writing combined barriers to H5")
    io_handler.write_layer(combined, merge_config.output_layer_name)


build_routing_layers_command = CLICommandFromFunction(
    build_routing_layers,
    name="build-routing-layers",
    add_collect=False,
    split_keys=None,
)
