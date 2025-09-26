"""
Integration modules for external libraries
==========================================

VizlyChart integrations with popular data science libraries.
"""

from .pandas_integration import *

__all__ = [
    'DataFrame',
    'plot_dataframe',
    'register_pandas_accessor',
]