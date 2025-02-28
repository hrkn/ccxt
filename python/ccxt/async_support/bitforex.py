# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange

# -----------------------------------------------------------------------------

try:
    basestring  # Python 3
except NameError:
    basestring = str  # Python 2
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import DDoSProtection


class bitforex (Exchange):

    def describe(self):
        return self.deep_extend(super(bitforex, self).describe(), {
            'id': 'bitforex',
            'name': 'Bitforex',
            'countries': ['CN'],
            'version': 'v1',
            'has': {
                'fetchBalance': True,
                'fetchMarkets': True,
                'createOrder': True,
                'cancelOrder': True,
                'fetchTicker': True,
                'fetchTickers': False,
                'fetchMyTrades': False,
                'fetchTrades': True,
                'fetchOrder': True,
                'fetchOrders': False,
                'fetchOpenOrders': True,
                'fetchClosedOrders': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/44310033-69e9e600-a3d8-11e8-873d-54d74d1bc4e4.jpg',
                'api': 'https://api.bitforex.com',
                'www': 'https://www.bitforex.com',
                'doc': 'https://github.com/bitforexapi/API_Docs/wiki',
                'fees': 'https://help.bitforex.com/en_us/?cat=13',
                'referral': 'https://www.bitforex.com/en/invitationRegister?inviterId=1867438',
            },
            'api': {
                'public': {
                    'get': [
                        'api/v1/market/symbols',
                        'api/v1/market/ticker',
                        'api/v1/market/depth',
                        'api/v1/market/trades',
                        'api/v1/market/kline',
                    ],
                },
                'private': {
                    'post': [
                        'api/v1/fund/mainAccount',
                        'api/v1/fund/allAccount',
                        'api/v1/trade/placeOrder',
                        'api/v1/trade/placeMultiOrder',
                        'api/v1/trade/cancelOrder',
                        'api/v1/trade/orderInfo',
                        'api/v1/trade/orderInfos',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': 0.1 / 100,
                    'taker': 0.1 / 100,
                },
                'funding': {
                    'tierBased': False,
                    'percentage': True,
                    'deposit': {},
                    'withdraw': {
                        'BTC': 0.0005,
                        'ETH': 0.01,
                        'BCH': 0.0001,
                        'LTC': 0.001,
                        'ETC': 0.005,
                        'USDT': 5,
                        'CMCT': 30,
                        'AION': 3,
                        'LVT': 0,
                        'DATA': 40,
                        'RHP': 50,
                        'NEO': 0,
                        'AIDOC': 10,
                        'BQT': 2,
                        'R': 2,
                        'DPY': 0.8,
                        'GTC': 40,
                        'AGI': 30,
                        'DENT': 100,
                        'SAN': 1,
                        'SPANK': 8,
                        'AID': 5,
                        'OMG': 0.1,
                        'BFT': 5,
                        'SHOW': 150,
                        'TRX': 20,
                        'ABYSS': 10,
                        'THM': 25,
                        'ZIL': 20,
                        'PPT': 0.2,
                        'WTC': 0.4,
                        'LRC': 7,
                        'BNT': 1,
                        'CTXC': 1,
                        'MITH': 20,
                        'TRUE': 4,
                        'LYM': 10,
                        'VEE': 100,
                        'AUTO': 200,
                        'REN': 50,
                        'TIO': 2.5,
                        'NGC': 1.5,
                        'PST': 10,
                        'CRE': 200,
                        'IPC': 5,
                        'PTT': 1000,
                        'XMCT': 20,
                        'ATMI': 40,
                        'TERN': 40,
                        'XLM': 0.01,
                        'ODE': 15,
                        'FTM': 100,
                        'RTE': 100,
                        'DCC': 100,
                        'IMT': 500,
                        'GOT': 3,
                        'EGT': 500,
                        'DACC': 1000,
                        'UBEX': 500,
                        'ABL': 100,
                        'OLT': 100,
                        'DAV': 40,
                        'THRT': 10,
                        'RMESH': 3,
                        'UPP': 20,
                        'SDT': 0,
                        'SHR': 10,
                        'MTV': 3,
                        'ESS': 100,
                        'MET': 3,
                        'TTC': 20,
                        'LXT': 10,
                        'XCLP': 100,
                        'LUK': 100,
                        'UBC': 100,
                        'DTX': 10,
                        'BEAT': 20,
                        'DEED': 2,
                        'BGX': 3000,
                        'PRL': 20,
                        'ELY': 50,
                        'CARD': 300,
                        'SQR': 15,
                        'VRA': 400,
                        'BWX': 3500,
                        'MAS': 75,
                        'FLP': 0.6,
                        'UNC': 300,
                        'CRNC': 15,
                        'MFG': 70,
                        'ZXC': 70,
                        'TRT': 30,
                        'ZIX': 35,
                        'XRA': 10,
                        'AMO': 1600,
                        'IPG': 3,
                        'uDoo': 50,
                        'URB': 30,
                        'ARCONA': 3,
                        'CRAD': 5,
                        'NOBS': 1000,
                        'ADF': 2,
                        'ELF': 5,
                        'LX': 20,
                        'PATH': 15,
                        'SILK': 120,
                        'SKYFT': 50,
                        'EDN': 50,
                        'ADE': 50,
                        'EDR': 10,
                        'TIME': 0.25,
                        'SPRK': 20,
                        'QTUM': 0.01,
                        'BF': 5,
                        'ZPR': 100,
                        'HYB': 10,
                        'CAN': 30,
                        'CEL': 10,
                        'ATS': 50,
                        'KCASH': 1,
                        'ACT': 0.01,
                        'MT': 300,
                        'DXT': 30,
                        'WAB': 4000,
                        'HYDRO': 400,
                        'LQD': 5,
                        'OPTC': 200,
                        'EQUAD': 80,
                        'LATX': 50,
                        'LEDU': 100,
                        'RIT': 70,
                        'ACDC': 500,
                        'FSN': 2,
                    },
                },
            },
            'exceptions': {
                '4004': OrderNotFound,
                '1013': AuthenticationError,
                '1016': AuthenticationError,
                '3002': InsufficientFunds,
                '10204': DDoSProtection,
            },
        })

    async def fetch_markets(self, params={}):
        response = await self.publicGetApiV1MarketSymbols(params)
        data = response['data']
        result = []
        for i in range(0, len(data)):
            market = data[i]
            id = self.safe_string(market, 'symbol')
            symbolParts = id.split('-')
            baseId = symbolParts[2]
            quoteId = symbolParts[1]
            base = self.safeCurrencyCode(baseId)
            quote = self.safeCurrencyCode(quoteId)
            symbol = base + '/' + quote
            active = True
            precision = {
                'amount': self.safe_integer(market, 'amountPrecision'),
                'price': self.safe_integer(market, 'pricePrecision'),
            }
            limits = {
                'amount': {
                    'min': self.safe_float(market, 'minOrderAmount'),
                    'max': None,
                },
                'price': {
                    'min': None,
                    'max': None,
                },
                'cost': {
                    'min': None,
                    'max': None,
                },
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    def parse_trade(self, trade, market=None):
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'time')
        id = self.safe_string(trade, 'tid')
        orderId = None
        amount = self.safe_float(trade, 'amount')
        price = self.safe_float(trade, 'price')
        cost = None
        if price is not None:
            if amount is not None:
                cost = amount * price
        sideId = self.safe_integer(trade, 'direction')
        side = self.parse_side(sideId)
        return {
            'info': trade,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'order': orderId,
            'fee': None,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        if limit is not None:
            request['size'] = limit
        market = self.market(symbol)
        response = await self.publicGetApiV1MarketTrades(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privatePostApiV1FundAllAccount(params)
        data = response['data']
        result = {'info': response}
        for i in range(0, len(data)):
            balance = data[i]
            currencyId = self.safe_string(balance, 'currency')
            code = self.safeCurrencyCode(currencyId)
            account = self.account()
            account['used'] = self.safe_float(balance, 'frozen')
            account['free'] = self.safe_float(balance, 'active')
            account['total'] = self.safe_float(balance, 'fix')
            result[code] = account
        return self.parse_balance(result)

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.markets[symbol]
        request = {
            'symbol': market['id'],
        }
        response = await self.publicGetApiV1MarketTicker(self.extend(request, params))
        data = response['data']
        timestamp = self.safe_integer(data, 'date')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(data, 'high'),
            'low': self.safe_float(data, 'low'),
            'bid': self.safe_float(data, 'buy'),
            'bidVolume': None,
            'ask': self.safe_float(data, 'sell'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': self.safe_float(data, 'last'),
            'last': self.safe_float(data, 'last'),
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_float(data, 'vol'),
            'quoteVolume': None,
            'info': response,
        }

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        marketId = self.market_id(symbol)
        request = {
            'symbol': marketId,
        }
        if limit is not None:
            request['size'] = limit
        response = await self.publicGetApiV1MarketDepth(self.extend(request, params))
        data = response['data']
        timestamp = response['time']
        bidsKey = 'bids'
        asksKey = 'asks'
        priceKey = 'price'
        amountKey = 'amount'
        orderbook = self.parse_order_book(data, timestamp, bidsKey, asksKey, priceKey, amountKey)
        return orderbook

    def parse_order_status(self, status):
        statuses = {
            '0': 'open',
            '1': 'open',
            '2': 'closed',
            '3': 'canceled',
            '4': 'canceled',
        }
        return statuses[status] if (status in list(statuses.keys())) else status

    def parse_side(self, sideId):
        if sideId == 1:
            return 'buy'
        elif sideId == 2:
            return 'sell'
        else:
            return None

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'orderId')
        timestamp = self.safe_float(order, 'createTime')
        lastTradeTimestamp = self.safe_float(order, 'lastTime')
        symbol = market['symbol']
        sideId = self.safe_integer(order, 'tradeType')
        side = self.parse_side(sideId)
        type = None
        price = self.safe_float(order, 'orderPrice')
        average = self.safe_float(order, 'avgPrice')
        amount = self.safe_float(order, 'orderAmount')
        filled = self.safe_float(order, 'dealAmount')
        remaining = amount - filled
        status = self.parse_order_status(self.safe_string(order, 'orderState'))
        cost = filled * price
        feeSide = 'base' if (side == 'buy') else 'quote'
        feeCurrency = market[feeSide]
        fee = {
            'cost': self.safe_float(order, 'tradeFee'),
            'currency': feeCurrency,
        }
        result = {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': lastTradeTimestamp,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'cost': cost,
            'average': average,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
        }
        return result

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': self.market_id(symbol),
            'orderId': id,
        }
        response = await self.privatePostApiV1TradeOrderInfo(self.extend(request, params))
        order = self.parse_order(response['data'], market)
        return order

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': self.market_id(symbol),
            'state': 0,
        }
        response = await self.privatePostApiV1TradeOrderInfos(self.extend(request, params))
        return self.parse_orders(response['data'], market, since, limit)

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': self.market_id(symbol),
            'state': 1,
        }
        response = await self.privatePostApiV1TradeOrderInfos(self.extend(request, params))
        return self.parse_orders(response['data'], market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        sideId = None
        if side == 'buy':
            sideId = 1
        elif side == 'sell':
            sideId = 2
        request = {
            'symbol': self.market_id(symbol),
            'price': price,
            'amount': amount,
            'tradeType': sideId,
        }
        response = await self.privatePostApiV1TradePlaceOrder(self.extend(request, params))
        data = response['data']
        return {
            'info': response,
            'id': self.safe_string(data, 'orderId'),
        }

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'orderId': id,
        }
        if symbol is not None:
            request['symbol'] = self.market_id(symbol)
        results = await self.privatePostApiV1TradeCancelOrder(self.extend(request, params))
        success = results['success']
        returnVal = {'info': results, 'success': success}
        return returnVal

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            payload = self.urlencode({'accessKey': self.apiKey})
            query['nonce'] = self.milliseconds()
            if query:
                payload += '&' + self.urlencode(self.keysort(query))
            # message = '/' + 'api/' + self.version + '/' + path + '?' + payload
            message = '/' + path + '?' + payload
            signature = self.hmac(self.encode(message), self.encode(self.secret))
            body = payload + '&signData=' + signature
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response):
        if not isinstance(body, basestring):
            return  # fallback to default error handler
        if (body[0] == '{') or (body[0] == '['):
            feedback = self.id + ' ' + body
            success = self.safe_value(response, 'success')
            if success is not None:
                if not success:
                    code = self.safe_string(response, 'code')
                    if code in self.exceptions:
                        raise self.exceptions[code](feedback)
                    else:
                        raise ExchangeError(feedback)
