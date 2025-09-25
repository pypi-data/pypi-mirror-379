# from .stats.smoothing import moving_average, ExponentialSmoother
# from .vis.palette import default_color_cycle

# __all__ = ["moving_average", "ExponentialSmoother", "default_color_cycle"]
# __version__ = "0.1.0"

from .orders import simulate_customer_orders, summarize_orders

__all__ = ["simulate_customer_orders", "summarize_orders"]
__version__ = "0.1.0"
