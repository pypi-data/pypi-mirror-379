# smeller/config/constants.py
from smeller.models.interpolation import InterpolationType

PLOT_WIDTH = 400
"""Width of the plot widget in pixels."""
PLOT_HEIGHT = 200
"""Height of the plot widget in pixels."""
MIN_TIME_STEP = 0.1 # Минимальный шаг по времени (секунды)
"""Minimum time step for waypoint adjustments."""
MIN_INTENSITY_STEP = 1 # Минимальный шаг по интенсивности (%)
"""Minimum intensity step for waypoint adjustments."""
MAX_CHANNELS = 12 # Максимальное количество каналов (картриджей)
"""Maximum number of channels supported."""
INTERPOLATION_POINTS = 100 # Количество точек для интерполяции между waypoints
"""Number of points used for interpolation between waypoints in the plot."""

LINEAR = InterpolationType.LINEAR
"""Constant for Linear interpolation type."""
EXPONENTIAL = InterpolationType.EXPONENTIAL
"""Constant for Exponential interpolation type."""
SINUSOIDAL = InterpolationType.SINUSOIDAL
"""Constant for Sinusoidal interpolation type."""
STEP = InterpolationType.STEP
"""Constant for Step interpolation type."""