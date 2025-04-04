import os
import asyncio
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_WALLET = Web3.to_checksum_address(os.getenv("MY_WALLET"))
GM_CONTRACT = "0x59c27c39A126a9B5eCADdd460C230C857e1Deb35"

web3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(PRIVATE_KEY)

async def send_gm():
    payload = "0x5011b71c"

    nonce = web3.eth.get_transaction_count(MY_WALLET)

    tx = {
        "from": MY_WALLET,
        "to": GM_CONTRACT,
        "data": payload,
        "value": web3.to_wei(0.0000001, "ether"),
        "gas": 300000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce,
        "chainId": 6342,
    }

    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Transaction sent. TX: https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/{tx_hash.hex()}")

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        print("✅ GM sent!")
    else:
        print("❌ GM sending error, most likely 24 hours haven't still passed.")


if __name__ == "__main__":
    asyncio.run(send_gm())
  
