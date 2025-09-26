"""
MLON - A comprehensive utility package for machine learning development
"""

from .preprocessing import DataPreprocessor
from .metrics import ModelEvaluator
from .visualization import Visualizer
from .model_utils import ModelUtils
from .cross_validation import CrossValidator
from .time_series import TimeSeriesUtils
from .feature_selection import FeatureSelector
from .guardrails import LeakageDetector, BiasDetector
from .auto_check import AutoChecker
from .cli import cli

__version__ = "1.2.0"
