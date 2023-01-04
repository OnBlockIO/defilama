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
def get_gas_prices(chain: Chain):
    gas_price = get_gas_price(chain)
    if chain != Chain.all:
        return [gas_price]
    elif chain == Chain.all:
        arr = []
        gasAvalanche = get_gas_price('avalanche')
        gasAvalanche['chain'] = 'avalanche'
        arr.append(gasAvalanche)
        gasEth = get_gas_price('eth')
        gasEth['chain'] = 'eth'
        arr.append(gasEth)
        gasPolygon = get_gas_price('polygon')
        gasPolygon['chain'] = 'polygon'
        arr.append(gasPolygon)
        gasBsc = get_gas_price('bsc')
        gasBsc['chain'] = 'bsc'
        arr.append(gasBsc)
        return arr
    else:
        raise HTTPException(status_code=403, detail="Chain not available")
