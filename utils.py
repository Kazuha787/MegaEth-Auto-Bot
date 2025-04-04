from web3 import Web3
from teko.config import RPC_URL

web3 = Web3(Web3.HTTPProvider(RPC_URL))

def get_nonce(address):
    return web3.eth.get_transaction_count(address, 'pending')

def get_gas_price():
    return web3.eth.gas_price