import asyncio
from typing import List
import requests_async as requests

from companies.adapter.quote_adapter import QuoteAdapter
from companies.interface.symbol_body import SymbolBody


class FinnhubApi:

    async def get_symbol(self, company_name: str) -> List[SymbolBody]:
        url = 'https://finnhub.io/api/v1/search?q={}&token=c3ntpfaad3iabnjjhoeg'.format(company_name)
        l = await requests.request(method='GET', url=url, json=True)
        return l.json()['result']

    async def get_quote(self, symbol: str) -> QuoteAdapter:
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token=c3ntpfaad3iabnjjhoeg'.format(symbol)
        result = await requests.get(url)
        return result.json()

    async def _parse_result(self, symbolq: SymbolBody):
        quote = await self.get_quote(symbolq.get('symbol'))
        symbolw = symbolq
        symbolw['quote'] = quote
        return symbolw

    async def list(self, query: str):
        symbol_list = await self.get_symbol(query)
        return await asyncio.gather(*[self._parse_result(symbol) for symbol in symbol_list])