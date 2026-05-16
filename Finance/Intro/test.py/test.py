import numpy as np
import sys
def get_trend(prices):
     avg_price = np.mean(prices)
     current_price = prices[-1]

     if avg_price > current_price:
          return "Bullish", avg_price - current_price
     
     else:
          return "Bearish", current_price - avg_price
     
def get_volatility(prices):
     std_dev = np.std(prices)

     if std_dev > 2:
          return "Volatile", std_dev
     
     else:
          return "Steady", std_dev

def project_price(current_price, trend_strength, volatility_value, news_bias, time_factor = 1):
     return current_price + (trend_strength * time_factor) * (volatility_value * news_bias)

def analyze_market(prices, news_bias = 0):
     trend, trend_strength = get_trend(prices)
     volatility_state, volatility_value = get_volatility(prices)

     current_price = prices[-1]

     projection = project_price(
          current_price,
          trend_strength,
          volatility_value,
          news_bias
     )
     return{
          "trend": trend,
          "volatility": volatility_state,
          "current_price": current_price,
          "Projection": projection
          

     }
     
try:
    x = int(5)

except NameError:
     print("There is a name error!")

else:
     print("Its all good!")
    

prices = [101, 103, 102, 105, 110, 121]
result = analyze_market(prices, news_bias = 0)

print(result)