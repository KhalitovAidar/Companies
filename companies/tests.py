from unittest import IsolatedAsyncioTestCase

from typing import List

import aiohttp
import requests

from companies.interface.symbol_body import SymbolBody
from stock_service.stock_api import FinnhubApi


class TestCompanies(IsolatedAsyncioTestCase):
    api = FinnhubApi()

    def test_one_plus_one_equal_two(self):
        list = self.api.list(query='apple')
        self.assertEqual(1 + 1, 2)

    async def test_symbol(self):
        l = await self.api.list('apple')
        self.assertEqual(1 + 1, 2)



