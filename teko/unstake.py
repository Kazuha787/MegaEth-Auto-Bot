import asyncio
from web3 import Web3
from teko.config import MY_WALLET, PRIVATE_KEY, TEKO_STAKING_CONTRACT, TKUSDC_POOL_ID, CHAIN_ID
from teko.abi import TEKO_ABI
from utils import web3, get_nonce, get_gas_price

async def unstake_tkusdc():
    contract = web3.eth.contract(address=TEKO_STAKING_CONTRACT, abi=TEKO_ABI)
    balance = contract.functions.getAssetsOf(TKUSDC_POOL_ID, MY_WALLET).call()
    print(f"Available for unstake: {balance / 10**6} USDC")
    if balance == 0:
        print("❌ No tkUSDC for unstake, skipping.")
        return

    unstake_txn = contract.functions.withdraw(
        TKUSDC_POOL_ID, balance, MY_WALLET, MY_WALLET
    ).build_transaction({
        'from': MY_WALLET,
        'nonce': get_nonce(MY_WALLET),
        'gas': 300000,
        'gasPrice': get_gas_price(),
        'chainId': CHAIN_ID
    })
    
    signed_unstake = web3.eth.account.sign_transaction(unstake_txn, PRIVATE_KEY)
    unstake_hash = web3.eth.send_raw_transaction(signed_unstake.raw_transaction)
    print(f"Unstake sent: https://web3.okx.com/ru/explorer/megaeth-testnet-explorer/tx/{unstake_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(unstake_hash)
    if receipt['status'] == 1:
        print("✅ Successfully unstaked!")
    else:
        print("❌ Unstaking error!")

if __name__ == "__main__":
    asyncio.run(unstake_tkusdc())
