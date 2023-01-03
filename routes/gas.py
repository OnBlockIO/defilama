from enum import Enum
from fastapi import APIRouter, HTTPException

from helpers.external_api import get_gas_price

router = APIRouter(
    prefix='/gas',
    tags=['Gas'],
)

class Chain(str, Enum):
    avalanche = "avalanche"
    eth = "eth"
    polygon = "polygon"
    bsc = "bsc"
    all = "all"

@router.get('/{chain}')
def get_gas_prices(chain: Chain | None):
    gas_price = get_gas_price(chain)
    if chain != Chain.all:
        return [gas_price]
    elif chain == Chain.all:
        arr = []
        arr.append(get_gas_price('avalanche'))
        arr.append(get_gas_price('eth'))
        arr.append(get_gas_price('polygon'))
        arr.append(get_gas_price('bsc'))
        return arr
    else:
        raise HTTPException(status_code=403, detail="Chain not available")
