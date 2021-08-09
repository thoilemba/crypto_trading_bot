import logging
import requests


logger = logging.getLogger()


def get_contract():

    contracts = []

    response_object = requests.get("https://testnet.binancefuture.com/fapi/v1/exchangeInfo")

    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts
