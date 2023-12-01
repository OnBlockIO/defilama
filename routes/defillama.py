from enum import Enum
from fastapi import APIRouter, HTTPException

from helpers.external_api import get_gm_price, get_monthly_volume, get_gm_stats
from helpers.blockchain import get_gm_in_gfund, get_gm_minted_per_sec

router = APIRouter(
    prefix='/defillama',
    tags=['DefiLlama'],
)

BASE_DATA = {
    "pool": "0xb91888ba149f267ad91817822bf2adaa0e3aa697",
    "chain": "Neo",
    "project": "ghostmarket",
    "symbol": "GFUND",
    "rewardTokens": [
        "0x9b049f1283515eef1d3f6ac610e1595ed25ca3e9"
    ],
    "underlyingTokens": [
        "0x9b049f1283515eef1d3f6ac610e1595ed25ca3e9"
    ],
    "poolMeta": "GhostMarket Single Stake Pool"
}

class Chain(str, Enum):
    avalanche = "avalanche"
    eth = "eth"
    polygon = "polygon"
    bsc = "bsc"
    pha = "pha"
    n3 = "n3"
    base = "base"

@router.get('/yield')
def get_yield():
    gm_price = get_gm_price()
    gm_minted_per_sec = get_gm_minted_per_sec()
    gm_in_flund = get_gm_in_gfund()
    monthly_volume = get_monthly_volume()

    tvl = gm_in_flund / 10 ** 8 * gm_price
    mint_apr = gm_minted_per_sec * 3600 * 24 * 365 / gm_in_flund * 100
    fee_apr = monthly_volume * 0.004 * 12 / tvl * 100

    BASE_DATA['tvlUsd'] = tvl
    BASE_DATA['apyBase'] = fee_apr
    BASE_DATA['apyReward'] = mint_apr

    return BASE_DATA

@router.get('/fees')
def get_fees(chain: Chain, timestamp: int):
    gm_stats = get_gm_stats(chain, timestamp)
    return gm_stats
