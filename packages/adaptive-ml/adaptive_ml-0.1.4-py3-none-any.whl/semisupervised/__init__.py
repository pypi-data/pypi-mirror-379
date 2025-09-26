# File: adaptive_ml_package/semi_supervised/__init__.py
#
# This file makes 'semi_supervised' a sub-package.
# It can expose modules like LabelPropagation.py.

# Example: Import all modules from the 'semi_supervised' directory
from . import LabelPropagation
from . import LabelSpreading

__all__ = ["LabelPropagation", "LabelSpreading"]