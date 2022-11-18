import requests

GM_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=ghostmarket&vs_currencies=usd"
GM_FEES_URL = "https://api.ghostmarket.io/api/v2/stats/chains?orderBy=MonthlyVolume&orderDirection=asc&page=1&size=50&getTotal=true&getWeeklyStats=true&getMonthlyStats=true&getTotalStats=false&localCurrency=USD&chain=n3"


def get_gm_price():
    res = requests.get(GM_PRICE_URL, verify=False).json()
    return res['ghostmarket']['usd']


def get_monthly_volume():
    res = requests.get(GM_FEES_URL, verify=False).json()
    return res['chains'][0]['monthly']['volume']
