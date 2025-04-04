import os
import json
import random
import asyncio
from web3 import Web3
from gte.abi import GTE_SWAPS_CONTRACT, GTE_TOKENS, GTE_SWAPS_ABI
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MY_WALLET = Web3.to_checksum_address(os.getenv("MY_WALLET"))

web3 = Web3(Web3.HTTPProvider(RPC_URL))

contract = web3.eth.contract(address=GTE_SWAPS_CONTRACT, abi=GTE_SWAPS_ABI)

WETH = web3.to_checksum_address(GTE_TOKENS["WETH"]["address"])
TOKENS = [(k, t["address"]) for k, t in GTE_TOKENS.items() if k != "WETH"]
random.shuffle(TOKENS)
random_token_name, random_token_address = random.choice(TOKENS)
random_token_address = web3.to_checksum_address(random_token_address)
slippage = 0.02


def approve(token_address, spender, amount):
    erc20_abi = json.loads('[{"constant": false, "inputs": [{"name": "spender", "type": "address"}, {"name": "value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}]')
    token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
    txn = token_contract.functions.approve(spender, amount).build_transaction({
        'from': MY_WALLET,
        'nonce': web3.eth.get_transaction_count(MY_WALLET),
        'gas': 100000,
        'gasPrice': web3.eth.gas_price
    })
    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print("Approve TX: https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/" + web3.to_hex(tx_hash))
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Approve done!")
        
def get_amount_out_min(amount_in, path):
    amounts = contract.functions.getAmountsOut(amount_in, path).call()
    amount_out_min = int(amounts[-1] * (1 - slippage))
    return amount_out_min

async def swap_tokens():
    TOKENS = [(k, t["address"]) for k, t in GTE_TOKENS.items() if k != "WETH"]
    random.shuffle(TOKENS)
    random_token_name, random_token_address = random.choice(TOKENS)
    random_token_address = web3.to_checksum_address(random_token_address)

    print(f"Selected token: {random_token_name} ({random_token_address})")

    balance = web3.eth.get_balance(MY_WALLET)
    swap_percentage = random.uniform(0.05, 0.15)
    amount_in_wei = int(balance * swap_percentage)

    print(f"Swapping {amount_in_wei} WETH -> {random_token_name}")

    def wrap_eth(amount_in_wei):
        weth_contract_abi = json.loads('[{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
        weth_contract = web3.eth.contract(address=WETH, abi=weth_contract_abi)
        nonce = web3.eth.get_transaction_count(MY_WALLET)

        txn = weth_contract.functions.deposit().build_transaction({
            'from': MY_WALLET,
            'value': amount_in_wei,
            'nonce': nonce,
            'gas': 100000,
            'gasPrice': web3.eth.gas_price
        })

        signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print("Wrap ETH TX:", web3.to_hex(tx_hash))
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Wrapping ETH to WETH completed!")

    wrap_eth(amount_in_wei)

    path = [WETH, random_token_address]
    amount_out_min = get_amount_out_min(amount_in_wei, path)

    approve(WETH, GTE_SWAPS_CONTRACT, amount_in_wei)

    nonce = web3.eth.get_transaction_count(MY_WALLET)
    transaction = contract.functions.swapExactTokensForTokens(
        amount_in_wei, amount_out_min, path, MY_WALLET, web3.eth.get_block('latest')['timestamp'] + 60
    ).build_transaction({
        'from': MY_WALLET,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price
    })

    signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print("Swap TX:", web3.to_hex(tx_hash))
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Swap done!")
    await asyncio.sleep(0)
    return tx_hash.hex()

def unwrap_all_eth():
    nonce = web3.eth.get_transaction_count(MY_WALLET)

    txn = {
        'from': MY_WALLET,
        'to': Web3.to_checksum_address("0x776401b9bc8aae31a685731b7147d4445fd9fb19"),
        'data': "0x2e1a7d4d",
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.eth.gas_price
    }

    weth_balance = web3.eth.call({
        'to': Web3.to_checksum_address("0x776401b9bc8aae31a685731b7147d4445fd9fb19"),
        'data': "0x70a08231000000000000000000000000" + MY_WALLET[2:]
    })

    weth_balance = int(weth_balance.hex(), 16)

    if weth_balance > 0:
        txn["data"] += hex(weth_balance)[2:].zfill(64)
        signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print("Unwrap ETH TX:", web3.to_hex(tx_hash))
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print("✅ Unwrapped all WETH to ETH!")
    else:
        print("No WETH balance to unwrap.")

async def swap_all_tokens_to_eth():
    unwrap_all_eth()
    for token_name, token_info in GTE_TOKENS.items():
        token_address = web3.to_checksum_address(token_info["address"])  
        
        if token_name == "WETH":
            continue

        token_contract = web3.eth.contract(
            address=token_address,
            abi=json.loads('[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
        )

        balance = token_contract.functions.balanceOf(MY_WALLET).call()

        if balance > 0:
            print(f"Swapping {balance} {token_name} to ETH")

            approve(token_address, GTE_SWAPS_CONTRACT, balance)
            path = [token_address, WETH]
            amount_out_min = get_amount_out_min(balance, path)

            transaction = contract.functions.swapExactTokensForTokens(
                balance, amount_out_min, path, MY_WALLET, web3.eth.get_block('latest')['timestamp'] + 60
            ).build_transaction({
                'from': MY_WALLET,
                'nonce': web3.eth.get_transaction_count(MY_WALLET),
                'gas': 200000,
                'gasPrice': web3.eth.gas_price
            })

            signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
            print(f"✅ Swap TX ({token_name}): https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/" + web3.to_hex(tx_hash))
            
            web3.eth.wait_for_transaction_receipt(tx_hash)
            await asyncio.sleep(0)

    print("✅ All tokens converted to ETH!")
  
