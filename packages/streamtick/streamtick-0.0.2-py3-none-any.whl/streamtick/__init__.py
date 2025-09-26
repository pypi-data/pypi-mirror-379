# Import the core UI function and give it a new name
from .ui import analyze_stock_ui as tick_arima

# You can also make other core functions available at the top level if needed
from .data_acquisition import get_stock_data_by_years
from .data_preprocessing import preprocess_data
from .arima import build_arima_models

# from streamtick import tick_arima - tick_arima()

# Expose the new ARIMA report component
from .arima_report import ArimaReport
# from streamtick import ArimaReport - ArimaReport()

