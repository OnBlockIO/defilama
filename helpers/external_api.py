import requests
import os

GM_PRICE_URL = "https://api.coingecko.com/api/v3/simple/price?ids=ghostmarket&vs_currencies=usd"
GM_FEES_URL = "https://api.ghostmarket.io/api/v2/stats/chains?orderBy=MonthlyVolume&orderDirection=asc&page=1&size=50&getTotal=true&getWeeklyStats=true&getMonthlyStats=true&getTotalStats=false&localCurrency=USD&chain=n3"
GM_STATS_URL = "https://api.ghostmarket.io/api/v2/stats/forperiod/chains"

MAPPING = {
    "avalanche": "avax",
    "eth": "ethereum",
    "polygon": "polygon",
    "bsc": "bsc",
    "pha": "phantasma",
    "n3": "neo"
}

def get_gm_price():
    print(requests.get(GM_PRICE_URL, verify=False).text)
    res = requests.get(GM_PRICE_URL, verify=False).json()
    return res['ghostmarket']['usd']

def get_monthly_volume():
    res = requests.get(GM_FEES_URL, verify=False).json()
    return res['chains'][0]['monthly']['volume']

def get_gm_stats(chain, start_timestamp):
    end_timestamp = start_timestamp + 3600 * 24
    res_day = requests.get(f"{GM_STATS_URL}?chain={chain}&startTimestamp={start_timestamp}&endTimestamp={end_timestamp}", verify=False).json()
    res_total = requests.get(f"{GM_STATS_URL}?chain={chain}", verify=False).json()
    return {
        "dailyFees": res_day['chains'][0]['forPeriod']['fees'],
        "userFees": res_total['chains'][0]['forPeriod']['fees'],
        "dailyRevenue": res_day['chains'][0]['forPeriod']['fees'],
        "protocolRevenue": res_total['chains'][0]['forPeriod']['fees'],
        "dailyVolume": res_day['chains'][0]['forPeriod']['volume'],
        "totalVolume": res_total['chains'][0]['forPeriod']['volume'],
    }