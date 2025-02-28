# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound


class bcex (Exchange):

    def describe(self):
        return self.deep_extend(super(bcex, self).describe(), {
            'id': 'bcex',
            'name': 'BCEX',
            'countries': ['CN', 'CA'],
            'version': '1',
            'has': {
                'fetchBalance': True,
                'fetchMarkets': True,
                'createOrder': True,
                'cancelOrder': True,
                'fetchTicker': True,
                'fetchTickers': False,
                'fetchTrades': True,
                'fetchOrder': True,
                'fetchOrders': True,
                'fetchClosedOrders': 'emulated',
                'fetchOpenOrders': True,
                'fetchTradingLimits': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/43362240-21c26622-92ee-11e8-9464-5801ec526d77.jpg',
                'api': 'https://www.bcex.top',
                'www': 'https://www.bcex.top',
                'doc': 'https://github.com/BCEX-TECHNOLOGY-LIMITED/API_Docs/wiki/Interface',
                'fees': 'https://bcex.udesk.cn/hc/articles/57085',
                'referral': 'https://www.bcex.top/register?invite_code=758978&lang=en',
            },
            'status': {
                'status': 'error',
                'updated': None,
                'eta': None,
                'url': None,
            },
            'api': {
                'public': {
                    'get': [
                        'Api_Market/getPriceList',  # tickers
                        'Api_Order/ticker',  # last ohlcv candle(ticker)
                        'Api_Order/depth',  # orderbook
                        'Api_Market/getCoinTrade',  # ticker
                        'Api_Order/marketOrder',  # trades...
                    ],
                    'post': [
                        'Api_Market/getPriceList',  # tickers
                        'Api_Order/ticker',  # last ohlcv candle(ticker)
                        'Api_Order/depth',  # orderbook
                        'Api_Market/getCoinTrade',  # ticker
                        'Api_Order/marketOrder',  # trades...
                    ],
                },
                'private': {
                    'post': [
                        'Api_Order/cancel',
                        'Api_Order/coinTrust',  # limit order
                        'Api_Order/orderList',  # open / all orders(my trades?)
                        'Api_Order/orderInfo',
                        'Api_Order/tradeList',  # open / all orders
                        'Api_Order/trustList',  # ?
                        'Api_User/userBalance',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'buy': 0.0,
                    'sell': 0.2 / 100,
                },
                'funding': {
                    'tierBased': False,
                    'percentage': False,
                    'withdraw': {
                        'ckusd': 0.0,
                        'other': 0.05 / 100,
                    },
                    'deposit': {},
                },
            },
            'exceptions': {
                '该币不存在,非法操作': ExchangeError,  # {code: 1, msg: "该币不存在,非法操作"} - returned when a required symbol parameter is missing in the request(also, maybe on other types of errors as well)
                '公钥不合法': AuthenticationError,  # {code: 1, msg: '公钥不合法'} - wrong public key
                '您的可用余额不足': InsufficientFunds,  # {code: 1, msg: '您的可用余额不足'} - your available balance is insufficient
                '您的btc不足': InsufficientFunds,  # {code: 1, msg: '您的btc不足'} - your btc is insufficient
                '参数非法': InvalidOrder,  # {'code': 1, 'msg': '参数非法'} - 'Parameter illegal'
                '订单信息不存在': OrderNotFound,  # {'code': 1, 'msg': '订单信息不存在'} - 'Order information does not exist'
            },
            'options': {
                'limits': {
                    # hardcoding is deprecated, using these predefined values is not recommended, use loadTradingLimits instead
                    'AFC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 6, 'max': 120000}}},
                    'AFC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 6, 'max': 120000}}},
                    'AFT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 15, 'max': 300000}}},
                    'AICC/CNET': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 5, 'max': 50000}}},
                    'AIDOC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 5, 'max': 100000}}},
                    'AISI/ETH': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.001, 'max': 500}}},
                    'AIT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 20, 'max': 400000}}},
                    'ANS/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.1, 'max': 500}}},
                    'ANS/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.1, 'max': 1000}}},
                    'ARC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 60, 'max': 600000}}},
                    'AXF/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 100, 'max': 1000000}}},
                    'BASH/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 250, 'max': 3000000}}},
                    'BATT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 60, 'max': 1500000}}},
                    'BCD/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 0.3, 'max': 7000}}},
                    'BHPC/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 2, 'max': 70000}}},
                    'BHPC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 2, 'max': 60000}}},
                    'BOPO/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 100, 'max': 2000000}}},
                    'BOPO/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 100, 'max': 10000000}}},
                    'BTC/CKUSD': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.001, 'max': 10}}},
                    'BTC/CNET': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.0005, 'max': 5}}},
                    'BTC/USDT': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.0002, 'max': 4}}},
                    'BTE/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 25, 'max': 250000}}},
                    'BU/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 20, 'max': 400000}}},
                    'CIC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 3000, 'max': 30000000}}},
                    'CIT/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 4, 'max': 40000}}},
                    'CIT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 4, 'max': 40000}}},
                    'CMT/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 5, 'max': 2500000}}},
                    'CNET/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 12, 'max': 120000}}},
                    'CNMC/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 4, 'max': 50000}}},
                    'CTC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 5, 'max': 550000}}},
                    'CZR/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 12, 'max': 500000}}},
                    'DCON/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 8, 'max': 300000}}},
                    'DCT/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 2, 'max': 40000}}},
                    'DCT/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 2, 'max': 2000}}},
                    'DOGE/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 3000, 'max': 14000000}}},
                    'DOGE/CKUSD': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 500, 'max': 2000000}}},
                    'DRCT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 16, 'max': 190000}}},
                    'ELA/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 0.02, 'max': 500}}},
                    'ELF/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 0.1, 'max': 100000}}},
                    'ELF/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 0.01, 'max': 100000}}},
                    'EOS/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.5, 'max': 5000}}},
                    'EOS/CNET': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 2.5, 'max': 30000}}},
                    'EOS/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 0.18, 'max': 1800}}},
                    'ETC/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.2, 'max': 2500}}},
                    'ETC/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.2, 'max': 2500}}},
                    'ETF/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 7, 'max': 150000}}},
                    'ETH/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.015, 'max': 100}}},
                    'ETH/CKUSD': {'precision': {'amount': 4, 'price': 4}, 'limits': {'amount': {'min': 0.005, 'max': 100}}},
                    'ETH/USDT': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.005, 'max': 100}}},
                    'FCT/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.24, 'max': 1000}}},
                    'FCT/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.24, 'max': 1000}}},
                    'GAME/CNET': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 1, 'max': 10000}}},
                    'GOOC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 200, 'max': 2000000}}},
                    'GP/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 600, 'max': 6000000}}},
                    'HSC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 1000, 'max': 20000000}}},
                    'IFISH/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 300, 'max': 8000000}}},
                    'IIC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 50, 'max': 4000000}}},
                    'IMOS/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 15, 'max': 300000}}},
                    'JC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 300, 'max': 3000000}}},
                    'LBTC/BTC': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 0.1, 'max': 3000}}},
                    'LEC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 500, 'max': 5000000}}},
                    'LKY/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 10, 'max': 70000}}},
                    'LKY/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 10, 'max': 100000}}},
                    'LMC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 25, 'max': 250000}}},
                    'LSK/CNET': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.3, 'max': 3000}}},
                    'LTC/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.01, 'max': 500}}},
                    'LTC/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.01, 'max': 500}}},
                    'LTC/USDT': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.02, 'max': 450}}},
                    'MC/CNET': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 10000, 'max': 100000000}}},
                    'MCC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 30, 'max': 350000}}},
                    'MOC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 25, 'max': 600000}}},
                    'MRYC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 300, 'max': 3000000}}},
                    'MT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 200, 'max': 6000000}}},
                    'MXI/CNET': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 5000, 'max': 60000000}}},
                    'NAI/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 10, 'max': 100000}}},
                    'NAS/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.2, 'max': 15000}}},
                    'NAS/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.5, 'max': 5000}}},
                    'NEWOS/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 65, 'max': 700000}}},
                    'NKN/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 3, 'max': 350000}}},
                    'NTK/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 2, 'max': 30000}}},
                    'ONT/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 0.2, 'max': 2000}}},
                    'ONT/ETH': {'precision': {'amount': 3, 'price': 8}, 'limits': {'amount': {'min': 0.01, 'max': 1000}}},
                    'PNT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 80, 'max': 800000}}},
                    'PST/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 5, 'max': 100000}}},
                    'PTT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 450, 'max': 10000000}}},
                    'QTUM/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.4, 'max': 2800}}},
                    'QTUM/CKUSD': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 0.1, 'max': 1000}}},
                    'RATING/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 500, 'max': 10000000}}},
                    'RHC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 1000, 'max': 10000000}}},
                    'SDA/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 20, 'max': 500000}}},
                    'SDD/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 10, 'max': 100000}}},
                    'SHC/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 250, 'max': 2500000}}},
                    'SHE/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 100, 'max': 5000000}}},
                    'SMC/CNET': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 1000, 'max': 10000000}}},
                    'SOP/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 50, 'max': 1000000}}},
                    'TAC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 35, 'max': 800000}}},
                    'TIP/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 7, 'max': 200000}}},
                    'TKT/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 40, 'max': 400000}}},
                    'TLC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 500, 'max': 10000000}}},
                    'TNC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 10, 'max': 110000}}},
                    'TUB/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 200, 'max': 8000000}}},
                    'UC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 100, 'max': 3000000}}},
                    'UDB/CNET': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 2000, 'max': 40000000}}},
                    'UIC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 5, 'max': 150000}}},
                    'VAAC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 10, 'max': 250000}}},
                    'VPN/CNET': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 200, 'max': 2000000}}},
                    'VSC/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 30, 'max': 650000}}},
                    'WAVES/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 0.15, 'max': 1500}}},
                    'WDNA/ETH': {'precision': {'amount': 2, 'price': 8}, 'limits': {'amount': {'min': 100, 'max': 250000}}},
                    'WIC/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 3, 'max': 30000}}},
                    'XAS/CNET': {'precision': {'amount': 2, 'price': 2}, 'limits': {'amount': {'min': 2.5, 'max': 25000}}},
                    'XLM/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 10, 'max': 300000}}},
                    'XLM/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 1, 'max': 300000}}},
                    'XLM/USDT': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 5, 'max': 150000}}},
                    'XRP/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 24, 'max': 100000}}},
                    'XRP/CKUSD': {'precision': {'amount': 2, 'price': 3}, 'limits': {'amount': {'min': 5, 'max': 50000}}},
                    'YBCT/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 15, 'max': 200000}}},
                    'YBCT/CKUSD': {'precision': {'amount': 2, 'price': 4}, 'limits': {'amount': {'min': 10, 'max': 200000}}},
                    'YBY/CNET': {'precision': {'amount': 2, 'price': 6}, 'limits': {'amount': {'min': 25000, 'max': 250000000}}},
                    'ZEC/BTC': {'precision': {'amount': 4, 'price': 8}, 'limits': {'amount': {'min': 0.02, 'max': 100}}},
                    'ZEC/CKUSD': {'precision': {'amount': 4, 'price': 2}, 'limits': {'amount': {'min': 0.02, 'max': 100}}},
                },
            },
        })

    async def fetch_trading_limits(self, symbols=None, params={}):
        # self method should not be called directly, use loadTradingLimits() instead
        # by default it will try load withdrawal fees of all currencies(with separate requests, sequentially)
        # however if you define symbols = ['ETH/BTC', 'LTC/BTC'] in args it will only load those
        await self.load_markets()
        if symbols is None:
            symbols = self.symbols
        result = {}
        for i in range(0, len(symbols)):
            symbol = symbols[i]
            result[symbol] = await self.fetch_trading_limits_by_id(self.market_id(symbol), params)
        return result

    async def fetch_trading_limits_by_id(self, id, params={}):
        request = {
            'symbol': id,
        }
        response = await self.publicPostApiOrderTicker(self.extend(request, params))
        #
        #     { code:    0,
        #         msg:   "获取牌价信息成功",
        #        data: {        high:  0.03721392,
        #                         low:  0.03335362,
        #                         buy: "0.03525757",
        #                        sell: "0.03531160",
        #                        last:  0.0352634,
        #                         vol: "184742.4176",
        #                   min_trade: "0.01500000",
        #                   max_trade: "100.00000000",
        #                number_float: "4",
        #                 price_float: "8"             }} }
        #
        return self.parse_trading_limits(self.safe_value(response, 'data', {}))

    def parse_trading_limits(self, limits, symbol=None, params={}):
        #
        #  {        high:  0.03721392,
        #             low:  0.03335362,
        #             buy: "0.03525757",
        #            sell: "0.03531160",
        #            last:  0.0352634,
        #             vol: "184742.4176",
        #       min_trade: "0.01500000",
        #       max_trade: "100.00000000",
        #    number_float: "4",
        #     price_float: "8"             }
        #
        return {
            'info': limits,
            'precision': {
                'amount': self.safe_integer(limits, 'number_float'),
                'price': self.safe_integer(limits, 'price_float'),
            },
            'limits': {
                'amount': {
                    'min': self.safe_float(limits, 'min_trade'),
                    'max': self.safe_float(limits, 'max_trade'),
                },
            },
        }

    async def fetch_markets(self, params={}):
        response = await self.publicGetApiMarketGetPriceList(params)
        result = []
        keys = list(response.keys())
        for i in range(0, len(keys)):
            currentMarketId = keys[i]
            currentMarkets = response[currentMarketId]
            for j in range(0, len(currentMarkets)):
                market = currentMarkets[j]
                baseId = self.safe_string(market, 'coin_from')
                quoteId = self.safe_string(market, 'coin_to')
                base = baseId.upper()
                quote = quoteId.upper()
                base = self.safeCurrencyCode(base)
                quote = self.safeCurrencyCode(quote)
                id = baseId + '2' + quoteId
                symbol = base + '/' + quote
                active = True
                defaults = self.safe_value(self.options['limits'], symbol, {})
                result.append(self.extend({
                    'id': id,
                    'symbol': symbol,
                    'base': base,
                    'quote': quote,
                    'baseId': baseId,
                    'quoteId': quoteId,
                    'active': active,
                    # overrided by defaults from self.options['limits']
                    'precision': {
                        'amount': None,
                        'price': None,
                    },
                    # overrided by defaults from self.options['limits']
                    'limits': {
                        'amount': {
                            'min': None,
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
                    },
                    'info': market,
                }, defaults))
        return result

    def parse_trade(self, trade, market=None):
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer_2(trade, 'date', 'created')
        if timestamp is not None:
            timestamp = timestamp * 1000
        id = self.safe_string(trade, 'tid')
        orderId = self.safe_string(trade, 'order_id')
        amount = self.safe_float_2(trade, 'number', 'amount')
        price = self.safe_float(trade, 'price')
        cost = None
        if price is not None:
            if amount is not None:
                cost = amount * price
        side = self.safe_string(trade, 'side')
        if side == 'sale':
            side = 'sell'
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
            request['limit'] = limit
        market = self.market(symbol)
        response = await self.publicPostApiOrderMarketOrder(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privatePostApiUserUserBalance(params)
        data = self.safe_value(response, 'data')
        keys = list(data.keys())
        result = {}
        for i in range(0, len(keys)):
            key = keys[i]
            amount = self.safe_float(data, key)
            parts = key.split('_')
            currencyId = parts[0]
            lockOrOver = parts[1]
            code = self.safeCurrencyCode(currencyId)
            if not(code in list(result.keys())):
                result[code] = self.account()
            if lockOrOver == 'lock':
                result[code]['used'] = float(amount)
            else:
                result[code]['free'] = float(amount)
        keys = list(result.keys())
        for i in range(0, len(keys)):
            key = keys[i]
            total = self.sum(result[key]['used'], result[key]['free'])
            result[key]['total'] = total
        result['info'] = data
        return self.parse_balance(result)

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.markets[symbol]
        request = {
            'part': market['quoteId'],
            'coin': market['baseId'],
        }
        response = await self.publicPostApiMarketGetCoinTrade(self.extend(request, params))
        timestamp = self.milliseconds()
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(response, 'max'),
            'low': self.safe_float(response, 'min'),
            'bid': self.safe_float(response, 'buy'),
            'bidVolume': None,
            'ask': self.safe_float(response, 'sale'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': self.safe_float(response, 'price'),
            'last': self.safe_float(response, 'price'),
            'previousClose': None,
            'change': None,
            'percentage': self.safe_float(response, 'change_24h'),
            'average': None,
            'baseVolume': self.safe_float(response, 'volume_24h'),
            'quoteVolume': None,
            'info': response,
        }

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        marketId = self.market_id(symbol)
        request = {
            'symbol': marketId,
        }
        response = await self.publicPostApiOrderDepth(self.extend(request, params))
        data = self.safe_value(response, 'data')
        timestamp = self.safe_integer(data, 'date')
        if timestamp is not None:
            timestamp *= 1000
        return self.parse_order_book(data, timestamp)

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = await self.privatePostApiOrderOrderList(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    def parse_order_status(self, status):
        statuses = {
            '0': 'open',
            '1': 'open',  # partially filled
            '2': 'closed',
            '3': 'canceled',
        }
        return self.safe_string(statuses, status, status)

    async def fetch_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrder requires a `symbol` argument')
        await self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
            'trust_id': id,
        }
        response = await self.privatePostApiOrderOrderInfo(self.extend(request, params))
        order = self.safe_value(response, 'data')
        timestamp = self.safe_integer(order, 'created')
        if timestamp is not None:
            timestamp *= 1000
        status = self.parse_order_status(self.safe_string(order, 'status'))
        side = self.safe_string(order, 'flag')
        if side == 'sale':
            side = 'sell'
        # Can't use parseOrder because the data format is different btw endpoint for fetchOrder and fetchOrders
        return {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': None,
            'side': side,
            'price': self.safe_float(order, 'price'),
            'cost': None,
            'average': self.safe_float(order, 'avg_price'),
            'amount': self.safe_float(order, 'number'),
            'filled': self.safe_float(order, 'numberdeal'),
            'remaining': self.safe_float(order, 'numberover'),
            'status': status,
            'fee': None,
        }

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'id')
        timestamp = self.safe_integer(order, 'datetime')
        if timestamp is not None:
            timestamp *= 1000
        symbol = None
        if market is not None:
            symbol = market['symbol']
        type = None
        side = self.safe_string(order, 'type')
        if side == 'sale':
            side = 'sell'
        price = self.safe_float(order, 'price')
        average = self.safe_float(order, 'avg_price')
        amount = self.safe_float(order, 'amount')
        remaining = self.safe_float(order, 'amount_outstanding')
        filled = amount - remaining
        status = self.parse_order_status(self.safe_string(order, 'status'))
        cost = filled * price
        fee = None
        result = {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
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

    async def fetch_orders_by_type(self, type, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        request = {
            'type': type,
        }
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        response = await self.privatePostApiOrderTradeList(self.extend(request, params))
        if 'data' in response:
            return self.parse_orders(response['data'], market, since, limit)
        return []

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_type('open', symbol, since, limit, params)

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        orders = await self.fetch_orders(symbol, since, limit, params)
        return self.filter_by(orders, 'status', 'closed')

    async def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_type('all', symbol, since, limit, params)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
            'type': side,
            'price': self.price_to_precision(symbol, price),
            'number': self.amount_to_precision(symbol, amount),
        }
        response = await self.privatePostApiOrderCoinTrust(self.extend(request, params))
        data = self.safe_value(response, 'data', {})
        id = self.safe_string(data, 'order_id')
        return {
            'info': response,
            'id': id,
        }

    async def cancel_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' cancelOrder requires a `symbol` argument')
        await self.load_markets()
        request = {}
        if symbol is not None:
            request['symbol'] = self.market_id(symbol)
        if id is not None:
            request['order_id'] = id
        return await self.privatePostApiOrderCancel(self.extend(request, params))

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        else:
            self.check_required_credentials()
            payload = self.urlencode({'api_key': self.apiKey})
            if query:
                payload += '&' + self.urlencode(self.keysort(query))
            auth = payload + '&secret_key=' + self.secret
            signature = self.hash(self.encode(auth))
            body = payload + '&sign=' + signature
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response):
        if response is None:
            return  # fallback to default error handler
        errorCode = self.safe_value(response, 'code')
        if errorCode is not None:
            if errorCode != 0:
                #
                # {code: 1, msg: "该币不存在,非法操作"} - returned when a required symbol parameter is missing in the request(also, maybe on other types of errors as well)
                # {code: 1, msg: '公钥不合法'} - wrong public key
                # {code: 1, msg: '价格输入有误，请检查你的数值精度'} - 'The price input is incorrect, please check your numerical accuracy'
                # {code: 1, msg: '单笔最小交易数量不能小于0.00100000,请您重新挂单'} -
                #                  'The minimum number of single transactions cannot be less than 0.00100000. Please re-post the order'
                #
                message = self.safe_string(response, 'msg')
                feedback = self.id + ' ' + message
                exceptions = self.exceptions
                if message in exceptions:
                    raise exceptions[message](feedback)
                elif message.find('请您重新挂单') >= 0:  # minimum limit
                    raise InvalidOrder(feedback)
                else:
                    raise ExchangeError(feedback)

    def calculate_fee(self, symbol, type, side, amount, price, takerOrMaker='taker', params={}):
        market = self.markets[symbol]
        rate = market[side]
        cost = float(self.cost_to_precision(symbol, amount * price))
        return {
            'type': takerOrMaker,
            'currency': market['quote'],
            'rate': rate,
            'cost': float(self.fee_to_precision(symbol, rate * cost)),
        }
