import requests
import warnings

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

GM_PRICE_URL = "https://api.flamingo.finance/token-info/prices"
GM_FEES_URL = "https://api.ghostmarket.io/api/v2/stats/chains?orderBy=MonthlyVolume&orderDirection=asc&page=1&size=50&getTotal=true&getWeeklyStats=true&getMonthlyStats=true&getTotalStats=false&localCurrency=USD&chain=n3"
GM_STATS_URL = "https://api.ghostmarket.io/api/v2/stats/forperiod/chains"

MAPPING = {
    "avalanche": "avax",
    "eth": "ethereum",
    "polygon": "polygon",
    "bsc": "bsc",
    "pha": "phantasma",
    "n3": "neo",
    "base": "base"
}


def get_gm_price():
    res = requests.get(GM_PRICE_URL, verify=False).json()
    for token_info in res:
        if token_info["symbol"] == "GM":
            return token_info['usd_price']


def get_monthly_volume():
    res = requests.get(GM_FEES_URL, verify=False).json()
    return res['chains'][0]['monthly']['volume']


def get_gm_stats(chain, start_timestamp):
    start_timestamp = start_timestamp - (start_timestamp % 86400)
    end_timestamp = start_timestamp + 3600 * 24
    res_day = requests.get(f"{GM_STATS_URL}?chain={chain}&startTimestamp={start_timestamp}&endTimestamp={end_timestamp}", verify=False).json()
    res_total = requests.get(f"{GM_STATS_URL}?chain={chain}", verify=False).json()
    if res_day['chains'] is None:
        return {
            "dailyFees": 0.0,
            "userFees": 0.0,
            "dailyRevenue": 0.0,
            "protocolRevenue": 0.0,
            "dailyVolume": 0.0,
            "totalVolume": 0.0,
        }
    else:
        return {
            "dailyFees": res_day['chains'][0]['forPeriod']['fees'],
            "userFees": res_total['chains'][0]['forPeriod']['fees'],
            "dailyRevenue": res_day['chains'][0]['forPeriod']['fees'],
            "protocolRevenue": res_total['chains'][0]['forPeriod']['fees'],
            "dailyVolume": res_day['chains'][0]['forPeriod']['volume'],
            "totalVolume": res_total['chains'][0]['forPeriod']['volume'],
        }
