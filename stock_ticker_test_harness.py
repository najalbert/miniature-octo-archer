from stock_ticker import StockTicker


NICK = 'nick'
IAN = 'ian'
YORI = 'yori'

ticker = StockTicker()

ticker.add_ticker(NICK)
ticker.add_ticker(IAN)
ticker.add_ticker(YORI)
ticker.update_price(YORI, 10)
ticker.update_price(NICK, 15)
ticker.update_price(YORI, 11)
ticker.update_price(NICK, 18)
ticker.update_price(NICK, 12)
ticker.update_price(YORI, 13)


low, high = ticker.get_price_extremes(NICK)
assert low == 12
assert high == 18
assert ticker.get_open_price(NICK) == 15
assert ticker.get_close_price(NICK) == 12
assert ticker.get_percent_change(NICK) == -20.0

low, high = ticker.get_price_extremes(YORI)
assert low == 10
assert high == 13
assert ticker.get_open_price(YORI) == 10
assert ticker.get_close_price(YORI) == 13
assert ticker.get_percent_change(YORI) == 30.0


low, high = ticker.get_price_extremes(IAN)
assert low is None
assert high is None
assert ticker.get_open_price(IAN) is None
assert ticker.get_close_price(IAN) is None
assert ticker.get_percent_change(IAN) is None
assert ticker.get_percent_change(IAN) is None


