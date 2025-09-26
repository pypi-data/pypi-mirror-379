def f1():
    return """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()"""

def f2():
    return """np.random.seed(1)
months = pd.date_range(start='2020-01', periods=36, freq='M')"""

def f3():
    return """seasonality = 10 + 5 * np.sin(2 * np.pi * (months.month - 1) / 12)
noise = np.random.normal(0, 1, len(months))
sales = seasonality + noise

data = pd.DataFrame({'Date': months, 'Umbrella_Sales': sales})
data.set_index('Date', inplace=True)"""

def f4():
    return """plt.figure(figsize=(10,4))
plt.plot(data, label='Umbrella Sales')
plt.title('Synthetic Monthly Umbrella Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()"""

def f5():
    return """model = ARIMA(data, order=(1,1,1))
model_fit = model.fit()"""

def f6():
    return """forecast_steps = 12
forecast = model_fit.forecast(steps=forecast_steps)

forecast_index = pd.date_range(start=data.index[-1] + pd.offsets.MonthEnd(1),
                               periods=forecast_steps, freq='M')
forecast_series = pd.Series(forecast, index=forecast_index)"""

def f7():
    return """plt.figure(figsize=(12,6))
plt.plot(data, label='Historical Sales')
plt.plot(forecast_series, label='Forecasted Sales', color='orange')
plt.title('Umbrella Sales Forecast (ARIMA Model)')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()"""



def f():
    return "Practical 6: ARIMA Time Series Forecasting (Umbrella Sales)"
