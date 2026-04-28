import numpy as np

def get_trend(prices):
    avg_price = np.mean(prices)
    current_price = prices[-1]

    if current_price > avg_price:
        return "Bullish", current_price - avg_price,
    else:
        return "Bearish" , avg_price - current_price

def get_volatility(prices):
    std_dev = np.std(prices)

    if std_dev > 2:
        return "Volatile" , std_dev
    else:
        return "Steady", std_dev

def project_price(current_price, trend_strength, volatility, news_bias, time_factor=1):
    return current_price + (trend_strength * time_factor) + (volatility * news_bias)

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
        "trend":trend,
        "volatility": volatility_state,
        "current_price": current_price,
        "projected_state": projection
    }

prices = [100, 102, 101, 105, 110]
result = analyze_market(prices, news_bias = 0 )

print(result)