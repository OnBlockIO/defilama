import requests

def get_gm_minted_per_sec(server="http://seed1.neo.org:10332"):
    payload = {
        "jsonrpc": "2.0",
        "method": "invokefunction",
        "params": ["0xb91888ba149f267ad91817822bf2adaa0e3aa697", "getProfitSpeed", [], []],
        "id": 1
    }
    res = requests.post(server, json=payload, verify=False).json()
    return int(res['result']['stack'][0]['value'])


def get_gm_in_gfund(server="http://seed1.neo.org:10332"):
    payload = {
      "id": 1,
      "jsonrpc": "2.0",
      "method": "invokefunction",
      "params": [
        "0x9b049f1283515eef1d3f6ac610e1595ed25ca3e9",
        "balanceOf",
        [{"type": "Hash160", "value": "b91888ba149f267ad91817822bf2adaa0e3aa697"}]
      ]
    }
    res = requests.post(server, json=payload, verify=False).json()
    return int(res['result']['stack'][0]['value'])


def get_gfund_supply(server="http://seed1.neo.org:10332"):
    payload = {
      "id": 1,
      "jsonrpc": "2.0",
      "method": "invokefunction",
      "params": [
        "0xb91888ba149f267ad91817822bf2adaa0e3aa697",
        "totalSupply",
        []
      ]
    }
    res = requests.post(server, json=payload, verify=False).json()
    return int(res['result']['stack'][0]['value'])
