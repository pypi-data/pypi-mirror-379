"""Doweb viewer."""

import os

__version__ = "1.6.1"

GFP_DOWEB_HTTPS = (
    os.environ.get("GFP_DOWEB_HTTPS", os.environ.get("GFP_KWEB_HTTPS", "false")).strip()
    == "true"
)
