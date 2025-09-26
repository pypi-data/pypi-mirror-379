# File: adaptive_ml_package/supervised/__init__.py
#
# This file makes 'supervised' a sub-package.
# It can expose modules like KNN.py.

# Example: Import all modules from the 'supervised' directory
from . import KNN

__all__ = ["KNN"]