import ccxt

#Replace the keys with your own
api_key = 'API_KEY'
secret =  'SECRET_KEY'

exchange = ccxt.bitmex({
    'apiKey': api_key ,
    'secret': secret ,
    'enableRateLimit': True,  # enable built-in rate limiter
})

#For testing on testnet only
#Remove or comment out before using on real api
exchange.urls['api'] = exchange.urls['test']

#Connection Test
print(exchange.id, exchange.load_markets())
