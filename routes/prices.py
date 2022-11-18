from enum import Enum
from fastapi import APIRouter, HTTPException

from helpers.external_api import get_gm_price
from helpers.blockchain import get_gm_in_gfund, get_gfund_supply


router = APIRouter(
    prefix='/prices',
    tags=['Prices'],
)


class Token(str, Enum):
    gm = "gm"
    gfund = "gfund"


@router.get('/{token}')
def get_price(token: Token):
    gm_price = get_gm_price()
    if token == Token.gm:
        return {
            "price": gm_price
        }
    elif token == Token.gfund:
        ratio = get_gm_in_gfund() / get_gfund_supply()
        return {
            "price": ratio * gm_price
        }
    else:
        raise HTTPException(status_code=403, detail="Token not available")
