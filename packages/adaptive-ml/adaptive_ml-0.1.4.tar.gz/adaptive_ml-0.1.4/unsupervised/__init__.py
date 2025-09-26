# File: adaptive_ml_package/unsupervised/__init__.py
#
# This file makes 'unsupervised' a sub-package.
# It can be used to expose the modules within it, like DBSCAN.py.

# Example: Import all modules from the 'unsupervised' directory
# The `*` in the import statement makes all public objects from
# these modules available when a user imports 'unsupervised'.
from . import DBSCAN
from . import Isomap
from . import UMAP

# You can also explicitly list what to expose with __all__
__all__ = ["DBSCAN", "Isomap", "UMAP"]
