import requests
import os
from dotenv import load_dotenv



load_dotenv()
API_KEY = os.getenv('API_KEY')

ticker = 'AAPL'
metric_dictionary = {}
time_period = 'annual' # annual, quarter
from_date = '2023-10-10'
to_date = '2024-08-10'

## ECONOMIC INDICATORS THAT WOULD BE USEFUL: 
# GDP, realGDP, nominalPotentialGDP, realGDPPerCapita, federalFunds, CPI, inflationRate, inflation, 
# retailSales, consumerSentiment, durableGoods, unemploymentRate, totalNonfarmPayroll, initialClaims, 
# industrialProductionTotalIndex, newPrivatelyOwnedHousingUnitsStartedTotalUnits, totalVehicleSales, 
# retailMoneyFunds, smoothedUSRecessionProbabilities, 3MonthOr90DayRatesAndYieldsCertificatesOfDeposit, 
# commercialBankInterestRateOnCreditCardPlansAllAccounts, 30YearFixedRateMortgageAverage, 
# 15YearFixedRateMortgageAverage

## urls that require upgraded account
## SEE https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements
# https://financialmodelingprep.com/api/v4/governance/executive_compensation?symbol=AAPL
# https://financialmodelingprep.com/api/v4/company-notes?symbol=AAPL
# https://financialmodelingprep.com/api/v4/historical/employee_count?symbol=AAPL
# https://financialmodelingprep.com/api/v4/employee_count?symbol=AAPL
# https://financialmodelingprep.com/api/v3/grade/AAPL
# https://financialmodelingprep.com/api/v3/key-executives/AAPL
# https://financialmodelingprep.com/api/v4/company-core-information?symbol=AAPL
# https://financialmodelingprep.com/api/v3/analyst-estimates/AAPL
# https://financialmodelingprep.com/api/v4/company-outlook?symbol=AAPL
# https://financialmodelingprep.com/api/v4/stock_peers?symbol=AAPL
# https://financialmodelingprep.com/api/v3/ratios/AAPL?period=quarter ## This one would be nice ##
# https://financialmodelingprep.com/api/v4/score?symbol=AAPL
# https://financialmodelingprep.com/api/v4/price-target?symbol=AAPL
# https://financialmodelingprep.com/api/v4/price-target-consensus?symbol=AAPL
# https://financialmodelingprep.com/api/v4/price-target-rss-feed?page=0
# https://financialmodelingprep.com/api/v4/upgrades-downgrades-consensus?symbol=AAPL
# https://financialmodelingprep.com/api/v4/upgrades-downgrades-grading-company?company=Barclay
# https://financialmodelingprep.com/api/v3/earning_call_transcript/AAPL?year=2020&quarter=3
# upcoming_stock_splits = f'https://financialmodelingprep.com/api/v3/stock_split_calendar?from={from_date}&to={to_date}&apikey={API_KEY}'
# https://financialmodelingprep.com/api/v4/standard_industrial_classification/all 

# paged urls
# fmp_articls_url = f'https://financialmodelingprep.com/api/v3/fmp/articles?page=0&size=5'
# https://financialmodelingprep.com/api/v4/general_news?page=0
# https://financialmodelingprep.com/api/v3/stock_news?page=0
# https://financialmodelingprep.com/api/v3/press-releases/AAPL


# url variables
discounted_cashflow_url = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{ticker}?apikey={API_KEY}'
income_statement_url = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period={time_period}&apikey={API_KEY}'
advanced_dcf_url = f'https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={ticker}&apikey={API_KEY}'
name_url = f'https://financialmodelingprep.com/api/v3/search-name?query={ticker}&limit=10&exchange=NASDAQ&apikey={API_KEY}'
company_profile_url = f'https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={API_KEY}'
market_cap_url = f'https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={API_KEY}'
historical_market_cap_url = f'https://financialmodelingprep.com/api/v3/historical-market-capitalization/{ticker}?limit=100&from=2023-10-10&to=2023-12-10&apikey={API_KEY}'
all_countries_url = f'https://financialmodelingprep.com/api/v3/get-all-countries?apikey={API_KEY}'
company_rating_url = f'https://financialmodelingprep.com/api/v3/rating/{ticker}?apikey={API_KEY}'
historical_rating_url = f'https://financialmodelingprep.com/api/v3/historical-rating/{ticker}?apikey={API_KEY}'
delisted_companies_url = f'https://financialmodelingprep.com/api/v3/delisted-companies?apikey={API_KEY}'
quote_order_url = f'https://financialmodelingprep.com/api/v3/quote-order/{ticker}?apikey={API_KEY}'
stock_price_change_url = f'https://financialmodelingprep.com/api/v3/stock-price-change/{ticker}?apikey={API_KEY}'
balance_statement_url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?period={time_period}&apikey={API_KEY}'
cashflow_statement_url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period={time_period}&apikey={API_KEY}'
statement_analysis_url = f'https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?period={time_period}&apikey={API_KEY}'
key_metrics_ttm = f'https://financialmodelingprep.com/api/v3/key-metrics-ttm/{ticker}apikey={API_KEY}'
ratios_ttm = f'https://financialmodelingprep.com/api/v3/ratios-ttm/{ticker}?apikey={API_KEY}'
earnings_surprises_url = f'https://financialmodelingprep.com/api/v3/earnings-surprises/{ticker}?apikey={API_KEY}'
dividend_calendar_historical = f'https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{ticker}?apikey={API_KEY}'

# calendar urls
dividend_calendar_url = f'https://financialmodelingprep.com/api/v3/stock_dividend_calendar?from={from_date}&to={to_date}&apikey={API_KEY}'




response = requests.request("GET", upcoming_stock_splits)

print(response.text)