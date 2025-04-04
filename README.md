![images](https://github.com/user-attachments/assets/d048a3b3-1e6c-4424-8abd-796b7dc2d6cd)


# ⚡ MegaETH Auto Bot by [Kazuha](https://github.com/Kazuha787) ⚡
# ⚡ Telegram [CHANNEL](https://t.me/Offical_Im_kazuha)

A spicy little automation tool for swapping, staking, minting, and other degen activities on the **MegaETH testnet** — powered by `Kazuha787` vibes and Gen Z ambition.

---

## 🚀 Features
- Automated token swaps & mints  
- Infinite loop mode or one-shot runs  
- Full `.env` support for safety  
- Easily customizable actions  
- Totally testnet-friendly, no real ETH harmed

---

## 🛠️ Installation

1. Clone this sexy beast:
 ```bash
 git clone https://github.com/Kazuha787/MegaEth-Auto-Bot.git
 cd MegaEth-Auto-Bot
   ```

3. Install the Python dependencies:
```sh
pip install -r requirements.txt
```

3. Edit  the env file:
```sh
nano .env
```

4. Add your wallet address and private key to the .env file.
(Treat it like your diary — don’t leak it.)


5. Customize your actions if you're feeling adventurous. Or keep the default config and let the bot cook.

## 🛠️ All Available Actions

These are the functions you can plug into the `ACTIONS` array in your `actions.py`. Mix, match, and stack them however you want depending on your mode of operation.

Each action is defined as a tuple:
```python
("Action Name", function_reference, True/False)
```

---

### ✅ Available Actions

```python
("tkUSDC staking", stake_tkusdc, True)        # Stake tkUSDC via Teko  
("tkUSDC unstaking", unstake_tkusdc, True)    # Unstake tkUSDC via Teko  
("Mint cUSD", mint_cusd, False)               # Mint cUSD token  
("Random Swap", swap_tokens, True)            # Random token swaps via gte  
("Swap all to ETH", swap_all_tokens_to_eth, True) # Convert all tokens to ETH  
("Send GM", send_gm, True)                    # Send GM via onchaingm (once every 24h)  
```

---

### ⚙️ How to Use

To customize your actions, open `actions.py` and find the `ACTIONS` array. Just edit it like this:

```python
ACTIONS = [
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("tkUSDC staking", stake_tkusdc, True),
    ("Swap all to ETH", swap_all_tokens_to_eth, True),
]
```

The third value (`True` or `False`) tells the bot whether the action should loop or only run once.  
Simple setup. Maximum control.

## ⚙️ Modes of Operation

The MegaETH-Auto-Bot gives you full control with three dynamic modes. Whether you're testing, farming, or going full degen — this bot’s got a mode for every mission.

---

### 🔹 Mode 1: Single Execution  
Executes your custom actions (from `actions.py`) **once**, in the exact order you define.

- Great for testing  
- Perfect for controlled runs  
- No loops, just precision

```python
ACTIONS = [
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("Swap all to ETH", swap_all_tokens_to_eth, True),
]
```

---

### 🔸 Mode 2: Infinite Randomizer  
Executes **random actions endlessly** from your `ACTIONS` list. Pure chaos farming.

- Simulates human-like behavior  
- Mixes things up  
- Runs forever (until you stop it)

```python
# Actions list can be the same
ACTIONS = [
    ("tkUSDC staking", stake_tkusdc, True),
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
]
```

---

### 🔹 Mode 3: Infinite Ordered Loop  
Executes your chosen actions in order, **on repeat**. Like Mode 1, but looped forever.

- Ideal for consistent farming  
- Useful for routine task grinding  
- Set it and forget it

```python
ACTIONS = [
    ("tkUSDC staking", stake_tkusdc, True),
    ("tkUSDC unstaking", unstake_tkusdc, True),
    ("Random Swap", swap_tokens, True),
]
```

---

### 🧠 How to Select the Mode

In `main.py`, you'll be asked to choose your mode:

```python
mode = int(input("Choose a mode (1 - One-time | 2 - Random Loop | 3 - Ordered Loop): "))
```

> Want it to auto-pick from `.env`? You can code that too. Let me know if you want help setting that up.
>
## Run The Bot Now 
```sh
python main.py
```

---

## ⭐ Support This Project

If this repo helped you save time, learn something new, or automate the grind — consider showing some love:

- **Star** this repo  
- **Follow** me for more tools  
- **Fork** it and make it yours  
- **Pull Requests** are always welcome — contribute like a boss!

Let's build better tools for Web3, together.

> [GitHub Profile](https://github.com/Kazuha787)  
> [Telegram](https://t.me/Offical_Im_kazuha)

---

## 📄 License

This project is licensed under the **MIT License** — do whatever you want, just don’t blame me when you break the chain.

```
MIT License

Copyright (c) 2025 Kazuha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

---

Thanks for checking out **MegaETH-Auto-Bot**. Stay decentralized, stay awesome.
