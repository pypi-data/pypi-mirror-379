import pytest
from datetime import date, timedelta
from moexalgo import session, Stock, Market, Futures

today = date.today()


def test_market(apikey):
    session.TOKEN = apikey
    eq = Market('EQ')
    assert eq == Market('shares')
    assert eq == Market('shares', 'TQBR')
    tickers = eq.tickers(use_dataframe=False)
    assert len([ticker for ticker in tickers]) > 50


def test_candles(apikey):
    session.TOKEN = apikey
    MOEX = Stock('MOEX')
    it = MOEX.candles(start=today, end=today, latest=True, use_dataframe=False)
    next(it)


def test_trades(apikey):
    session.TOKEN = apikey
    MOEX = Stock('MOEX')
    it = MOEX.trades(use_dataframe=False)
    trade = next(it)
    assert 'TRADENO' in trade


def test_tradestats(apikey):
    session.TOKEN = apikey
    EQ = Market('EQ')
    it = EQ.tradestats(date=today, use_dataframe=False)
    tradestat = next(it)
    assert tradestat.ts.date() == today
    assert 'disb' in tradestat
    assert next(it)

    MOEX = Stock('MOEX')
    it = MOEX.tradestats(start=today, end=today, latest=True, use_dataframe=False)
    tradestat = next(it)
    assert tradestat.ts.date() == today
    assert 'disb' in tradestat


def test_orderstats(apikey):
    session.TOKEN = apikey
    EQ = Market('EQ')
    it = EQ.orderstats(date=today, use_dataframe=False)
    orderstat = next(it)
    assert orderstat.ts.date() == today
    assert 'put_vwap_s' in orderstat
    assert next(it)

    MOEX = Stock('MOEX')
    it = MOEX.orderstats(start=today, end=today, latest=True, use_dataframe=False)
    orderstat = next(it)
    assert orderstat.ts.date() == today
    assert 'put_vwap_b' in orderstat


def test_obstats(apikey):
    session.TOKEN = apikey
    EQ = Market('EQ')
    it = EQ.obstats(date=today, use_dataframe=False)
    obstat = next(it)
    assert obstat.ts.date() == today
    assert 'spread_bbo' in obstat
    assert next(it)

    MOEX = Stock('MOEX')
    it = MOEX.obstats(start=today, end=today, latest=True, use_dataframe=False)
    obstat = next(it)
    assert obstat.ts.date() == today
    assert 'spread_1mio' in obstat


def test_futoi(apikey):
    session.TOKEN = apikey
    _14_day = today - timedelta(days=14)
    FO = Market('FO')
    it = FO.futoi(date=_14_day, use_dataframe=False)
    futoi = next(it)
    assert futoi.ts.date() == _14_day
    assert 'pos_short' in futoi
    assert next(it)
