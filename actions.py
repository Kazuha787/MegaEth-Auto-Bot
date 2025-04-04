from teko.stake import stake_tkusdc
from teko.unstake import unstake_tkusdc
from cap.cap import mint_cusd
from gte.gte import swap_tokens, swap_all_tokens_to_eth
from onchaingm.onchaingm import send_gm

ACTIONS = [
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("Random Swap", swap_tokens, True),
    ("tkUSDC staking", stake_tkusdc, True),
    ("Swap all to ETH", swap_all_tokens_to_eth, True),
]

"""
-----------------РУССКИЙ ЯЗЫК-----------------

Вы можете создавать свои цепочки действий добавляя или удаляя новые строки в ACTIONS:

ACTIONS = [
    ("Random Swap", swap_tokens, True),
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("tkUSDC staking", stake_tkusdc, True),
]

("tkUSDC staking", stake_tkusdc, True),
("tkUSDC unstaking", unstake_tkusdc, True),
("Mint cUSD", mint_cusd, False),
("Random Swap", swap_tokens, True),
("Swap all to ETH", swap_all_tokens_to_eth, True),
("Send GM", send_gm, True),

tkUSDC staking = Стейкинг через Teko
tkUSDC unstaking = Анстейк через Teko
Mint cUSD = Минт cUSD
Random Swap = Рандомные свопы через gte
Swap all to ETH = Своп всех токенов в ETH
Send GM = Отправка gm через onchaingm (раз в 24 часа)




-----------------ENGLISH LANGUAGE-----------------

You can create your action chains by adding or deleting new rows in ACTIONS:
ACTIONS = [
    (“Random Swap”, swap_tokens, True),
    (“Mint cUSD”, mint_cusd, False),
    (“Send GM”, send_gm, True),
    (“tkUSDC staking”, stake_tkusdc, True),
]

(“tkUSDC staking”, stake_tkusdc, True),
(“tkUSDC unstaking”, unstake_tkusdc, True),
(“Mint cUSD”, mint_cusd, False),
(“Random Swap”, swap_tokens, True),
(“Swap all to ETH”, swap_all_tokens_to_eth, True),
(“Send GM”, send_gm, True),

tkUSDC staking = Staking via Teko
tkUSDC unstaking = Unstaking via Teko
Mint cUSD = Mint cUSD
Random Swap = Random Swaps via gte
Swap all to ETH = Swap all tokens to ETH
Send GM = Send gm via onchaingm (once every 24 hours)

"""


# do not touch zis pls :(
ALL_ACTIONS = [
    ("tkUSDC Staking", stake_tkusdc, True),
    ("tkUSDC Unstaking", unstake_tkusdc, True),
    ("Mint cUSD", mint_cusd, False),
    ("Random Swap", swap_tokens, True),
    ("Swap all to ETH", swap_all_tokens_to_eth, True),
    ("Send GM", send_gm, True),
]