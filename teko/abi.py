ERC20_ABI = [
    {"inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"name": "spender", "type": "address"}, {"name": "value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"name": "owner", "type": "address"}, {"name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}
]

STAKING_ABI = [
    {"type": "function", "name": "deposit", "inputs": [
        {"name": "poolId", "type": "uint256"},
        {"name": "assets", "type": "uint256"},
        {"name": "receiver", "type": "address"}
    ], "outputs": [{"name": "shares", "type": "uint256"}], "stateMutability": "nonpayable"}
]

TEKO_ABI = [
    {"type": "function", "name": "deposit", "inputs": [
        {"name": "poolId", "type": "uint256"},
        {"name": "assets", "type": "uint256"},
        {"name": "receiver", "type": "address"}
    ], "outputs": [{"name": "shares", "type": "uint256"}], "stateMutability": "nonpayable"},
    {"type": "function", "name": "getAssetsOf", "inputs": [
        {"name": "poolId", "type": "uint256"},
        {"name": "guy", "type": "address"}
    ], "outputs": [{"name": "", "type": "uint256"}], "stateMutability": "view"},
    {"type": "function", "name": "withdraw", "inputs": [
        {"name": "poolId", "type": "uint256"},
        {"name": "assets", "type": "uint256"},
        {"name": "receiver", "type": "address"},
        {"name": "owner", "type": "address"}
    ], "outputs": [{"name": "shares", "type": "uint256"}], "stateMutability": "nonpayable"},
    {"type": "function", "name": "borrow", "inputs": [
        {"name": "poolId", "type": "uint256"},
        {"name": "position", "type": "address"},
        {"name": "amt", "type": "uint256"}
    ], "outputs": [{"name": "borrowShares", "type": "uint256"}], "stateMutability": "nonpayable"}
]