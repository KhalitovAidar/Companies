from companies.interface.quote_body import QuoteBody


class QuoteAdapter(object):
    _raw_quote: QuoteBody

    def __init__(self, raw_quote: QuoteBody):
        self._raw_quote = raw_quote

    @property
    def current_price(self):
        return self._raw_quote['c']

    @property
    def high_price(self):
        return self._raw_quote['h']

    @property
    def open_price(self):
        return self._raw_quote['o']

    @property
    def low_price(self):
        return self._raw_quote['l']

    @property
    def prev_close_price(self):
        return self._raw_quote['pc']

    @property
    def time_stamp(self):
        return self._raw_quote['t']
