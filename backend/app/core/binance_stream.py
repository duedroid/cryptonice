from binance import AsyncClient, BinanceSocketManager

from .cache import cache


class BinanceStream:
    async def startup(self):
        self.active_symbols = []
        self.client = await AsyncClient.create()
        self.bm = BinanceSocketManager(self.client)
    
    async def start_ticker_listener(self, symbol):
        if symbol in self.active_symbols:
            return

        binance_symbol = symbol.replace('/', '')
        key = symbol.replace('/', '_').lower()
        self.active_symbols.append(symbol)
        async with self.bm.symbol_miniticker_socket(binance_symbol) as stream:
            while symbol in self.active_symbols:
                msg = await stream.recv()
                await cache.set_value(key, msg['c'])

    async def stop_ticker_listener(self, symbol):
        try:
            self.active_symbols.remove(symbol)
        except ValueError:
            pass
        
        key = symbol.replace('/', '_').lower()
        await cache.delete_value(key)


binance_stream = BinanceStream()


