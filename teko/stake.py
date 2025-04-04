import asyncio
from web3 import Web3
from teko.config import MY_WALLET, PRIVATE_KEY, TEKO_STAKING_CONTRACT, TKUSDC_ADDRESS, TKUSDC_POOL_ID, CHAIN_ID
from teko.abi import ERC20_ABI, STAKING_ABI
from utils import web3, get_nonce, get_gas_price

async def stake_tkusdc():
    token = web3.eth.contract(address=TKUSDC_ADDRESS, abi=ERC20_ABI)
    balance = token.functions.balanceOf(MY_WALLET).call()
    print(f"Current balance: {balance / 10**6} USDC")
    
    if balance == 0:
        print("❌ Balance is 0, skipping.")
        return
    
    allowance = token.functions.allowance(MY_WALLET, TEKO_STAKING_CONTRACT).call()
    if allowance < balance:
        print("Sending approve...")
        approve_txn = token.functions.approve(TEKO_STAKING_CONTRACT, 2**256 - 1).build_transaction({
            'from': MY_WALLET,
            'nonce': get_nonce(MY_WALLET),
            'gas': 100000,
            'gasPrice': get_gas_price(),
            'chainId': CHAIN_ID
        })
        signed_approve = web3.eth.account.sign_transaction(approve_txn, PRIVATE_KEY)
        approve_hash = web3.eth.send_raw_transaction(signed_approve.raw_transaction)
        print(f"Approve sent: https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/{approve_hash.hex()}")
        web3.eth.wait_for_transaction_receipt(approve_hash)
    
    print("Sending stake...")
    staking_contract = web3.eth.contract(address=TEKO_STAKING_CONTRACT, abi=STAKING_ABI)
    stake_txn = staking_contract.functions.deposit(TKUSDC_POOL_ID, balance, MY_WALLET).build_transaction({
        'from': MY_WALLET,
        'nonce': get_nonce(MY_WALLET),
        'gas': 250000,
        'gasPrice': get_gas_price(),
        'chainId': CHAIN_ID
    })
    signed_stake = web3.eth.account.sign_transaction(stake_txn, PRIVATE_KEY)
    stake_hash = web3.eth.send_raw_transaction(signed_stake.raw_transaction)
    print(f"Stake sent: https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/{stake_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(stake_hash)
    if receipt['status'] == 1:
        print("✅ Successfully staked!")
    else:
        print("❌ Staking error!")

if __name__ == "__main__":
    asyncio.run(stake_tkusdc())
