# ruff: noqa: N801
"""Custom Warning for reVRt"""

import logging


logger = logging.getLogger("revrt")


class revrtWarning(UserWarning):
    """Generic revrt Warning"""

    def __init__(self, *args, **kwargs):
        """Init exception and broadcast message to logger"""
        super().__init__(*args, **kwargs)
        if args:
            logger.warning(str(args[0]), stacklevel=2)


class revrtDeprecationWarning(revrtWarning, DeprecationWarning):
    """revrt deprecation warning"""
