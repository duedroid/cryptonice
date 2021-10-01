from binance import AsyncClient, BinanceSocketManager

from .redis import redis


class BinanceSocket:
    async def startup(self):
        self.is_active = False
        self.symbol_data = {}
        self.streams = []
        self.client = await AsyncClient.create()
    
    async def start_ticker_listener(self, symbols):
        self.set_streams_and_symbols(symbols)
        if len(self.streams) == 0:
            return

        self.is_active = True
        bm = BinanceSocketManager(self.client)
        async with bm.multiplex_socket(self.streams) as stream:
            while self.is_active:
                msg = await stream.recv()
                key = self.symbol_data.get(msg['data']['s'])
                await redis.set(key, msg['data']['c'], 3600)
    
    def set_streams_and_symbols(self, symbols):
        self.reset_data()

        for symbol in symbols:
            currency, bridge = symbol.split('/')
            self.streams.append(currency.lower() + bridge.lower() + '@miniTicker')
            self.symbol_data[currency + bridge] = ':1:price_{0}_{1}'.format(
                currency.lower(), bridge.lower()
            )

    def stop_ticker_listener(self):
        self.reset_data()
    
    def reset_data(self):
        self.is_active = False
        self.symbol_data = {}
        self.streams = []
    
    def is_symbol_change(self, symbols):
        new_symbols = [symbol.replace('/', '') for symbol in symbols]
        return set(self.symbol_data.keys()) != set(new_symbols)


binance_socket = BinanceSocket()