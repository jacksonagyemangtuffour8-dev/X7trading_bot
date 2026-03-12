# Configuration Settings for Trading Bot

# Signal Expiry Times
SIGNAL_EXPIRY = {
    'short-term': '5m',  # 5 minutes
    'medium-term': '30m',  # 30 minutes
    'long-term': '1h'  # 1 hour
}

# Trading Pairs
TRADING_PAIRS = [
    'BTC/USD',
    'ETH/USD',
    'XRP/USD'
]

# API Endpoints
API_ENDPOINTS = {
    'base_url': 'https://api.tradingplatform.com',
    'get_signals': '/v1/signals',
    'execute_trade': '/v1/trade'
}
