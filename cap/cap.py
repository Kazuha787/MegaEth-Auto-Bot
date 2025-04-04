import os
from web3 import Web3
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_WALLET = Web3.to_checksum_address(os.getenv("MY_WALLET"))

web3 = Web3(Web3.HTTPProvider(RPC_URL))

MINT_CONTRACT = Web3.to_checksum_address("0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f")
CHAIN_ID = 6342

mint_abi = json.loads("""
[
  {
    "inputs": [
      {"internalType": "address","name": "to","type": "address"},
      {"internalType": "uint256","name": "amount","type": "uint256"}
    ],
    "name": "mint",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
""")

contract = web3.eth.contract(address=MINT_CONTRACT, abi=mint_abi)

amount_to_mint = web3.to_wei(1000, "ether")

def mint_cusd():
    nonce = web3.eth.get_transaction_count(MY_WALLET)

    txn = contract.functions.mint(MY_WALLET, amount_to_mint).build_transaction({
        'from': MY_WALLET,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'chainId': CHAIN_ID
    })

    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print("Mint TX:", web3.to_hex(tx_hash))
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    if receipt.status == 1:
        print("cUSD minted!")
    else:
        print("❌ cUSD mint failed!")
