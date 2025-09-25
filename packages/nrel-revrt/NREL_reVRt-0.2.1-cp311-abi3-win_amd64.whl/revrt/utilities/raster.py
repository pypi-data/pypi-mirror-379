"""reVRt rasterization utilities"""

import logging
from functools import lru_cache

import geopandas as gpd
from rasterio import features

from revrt.constants import DEFAULT_DTYPE


logger = logging.getLogger(__name__)


@lru_cache(maxsize=8)
def _cached_file_read(fp):
    """Not sure if this is actually needed, but porting from reVX"""
    return gpd.read_file(fp)


def rasterize_shape_file(
    fname,
    width,
    height,
    transform,
    buffer_dist=None,
    all_touched=False,
    dest_crs=None,
    burn_value=1,
    boundary_only=False,
    dtype=DEFAULT_DTYPE,
):
    """Rasterize a vector layer

    Parameters
    ----------
    fname : str
        Full path to GPKG or shp file.
    width : int
        Width of output raster.
    height : int
        Height of output raster.
    transform : affine.Affine
        Affine transform for output raster.
    buffer_dist : float, optional
        Distance to buffer features in fname by. Same units as the
        template raster. By default, ``None``.
    all_touched : bool, default=False
        Set all cells touched by vector to 1. False results in less
        cells being set to 1. By default, ``False``.
    reproject_vector : bool, default=True
        Reproject CRS of vector to match template raster if ``True``.
        By default, ``True``.
    burn_value : int | float, default=1
        Value used to burn vectors into raster. By default, ``1``.
    boundary_only : bool, default=False
        If ``True``, rasterize boundary of vector.
        By default, ``False``.
    dtype : np.dtype, default="float32"
        Datatype to use. By default, ``float32``.

    Returns
    -------
    array-like
        Rasterized vector data
    """
    gdf = _cached_file_read(fname)

    if dest_crs is not None:
        logger.debug("Reprojecting vector")
        gdf = gdf.to_crs(crs=dest_crs)

    logger.debug("Rasterizing %s", fname)
    return rasterize(
        gdf,
        width,
        height,
        transform,
        buffer_dist=buffer_dist,
        all_touched=all_touched,
        burn_value=burn_value,
        boundary_only=boundary_only,
        dtype=dtype,
    )


def rasterize(
    gdf,
    width,
    height,
    transform,
    buffer_dist=None,
    all_touched=False,
    burn_value=1,
    boundary_only=False,
    dtype=DEFAULT_DTYPE,
):
    """Rasterize a vector layer

    Parameters
    ----------
    gdf : geopandas.DataFrame
        Geopandas DataFrame contains shapes to rasterize.
    width : int
        Width of output raster.
    height : int
        Height of output raster.
    transform : affine.Affine
        Affine transform for output raster.
    buffer_dist : float, optional
        Distance to buffer features in fname by. Same units as the
        template raster. By default, ``None``.
    all_touched : bool, default=False
        Set all cells touched by vector to 1. False results in less
        cells being set to 1. By default, ``False``.
    burn_value : int | float, default=1
        Value used to burn vectors into raster. By default, ``1``.
    boundary_only : bool, default=False
        If ``True``, rasterize boundary of vector.
        By default, ``False``.
    dtype : np.dtype, default="float32"
        Datatype to use. By default, ``float32``.

    Returns
    -------
    numpy.nd_array
        Rasterized vector data
    """

    if buffer_dist is not None:
        gdf = gdf.copy()
        logger.debug("Buffering shapes by %s", buffer_dist)
        gdf.geometry = gdf.geometry.buffer(buffer_dist)
        logger.debug("Buffering done. %d features before cleaning.", len(gdf))
        gdf = gdf[~gdf.is_empty]  # Negative buffer may result in empty feats
        logger.debug("%d features after removing empty features.", len(gdf))

    logger.debug("Rasterizing shapes")
    return features.rasterize(
        list(gdf.boundary if boundary_only else gdf.geometry),
        out_shape=(height, width),
        fill=0,
        out=None,
        transform=transform,
        all_touched=all_touched,
        default_value=burn_value,
        dtype=dtype,
    )
