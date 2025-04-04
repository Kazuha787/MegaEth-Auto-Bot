import asyncio
import random
import time
from actions import ACTIONS, ALL_ACTIONS
import os
from rich.console import Console
from rich.text import Text
from rich.progress import Progress
import sys

console = Console()

os.system("cls")

banner = Text("""
              ╔════════════════════════════════════════════════════╗
              ║                  MEGAETH SOFTWARE                  ║
              ║            Mega ETH Automation Bot:                ║
              ║  Telegra https://t.me/Offical_Im_kazuha            ║
              ║     GitHub: https://github.com/Kazuha787           ║
              ╠════════════════════════════════════════════════════╣
              ║                                                    ║
              ║  ██╗  ██╗ █████╗ ███████╗██╗   ██╗██╗  ██╗ █████╗  ║
              ║  ██║ ██╔╝██╔══██╗╚══███╔╝██║   ██║██║  ██║██╔══██╗ ║
              ║  █████╔╝ ███████║  ███╔╝ ██║   ██║███████║███████║ ║
              ║  ██╔═██╗ ██╔══██║ ███╔╝  ██║   ██║██╔══██║██╔══██║ ║
              ║  ██║  ██╗██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║ ║
              ║  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ║
              ║                                                    ║
              ╚════════════════════════════════════════════════════╝
              """, style="bold cyan")

console.print(banner)

def get_user_choice():
    console.print("\n[bold yellow]Choose mode:[/bold yellow]")
    console.print("1: User-defined procedure (from actions.py) [once]", style="green")
    console.print("2: Random (infinite loop with all actions)", style="blue")
    console.print("3: Infinite loop (user-defined actions in order)", style="magenta")
    
    choice = input("\nEnter your number: ")
    return choice

async def execute_actions(actions):
    for action_name, action_func, is_async in actions:
        console.print(f"\n🚀 [bold cyan]Executing:[/bold cyan] {action_name}...")
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=100)
            for _ in range(10):
                time.sleep(0.2)
                progress.update(task, advance=10)
        try:
            if is_async:
                result = await action_func()
            else:
                result = action_func()

            if isinstance(result, str):
                console.print(f"✅ [bold green]{action_name} done![/bold green] TX: {result}")
        except Exception as e:
            console.print(f"❌ [bold red]Error while executing:[/bold red] {action_name}: {e}")

        time.sleep(2)

async def main():
    choice = get_user_choice()

    if choice == "2":
        while True:
            tasks = ALL_ACTIONS.copy()
            random.shuffle(tasks)
            await execute_actions(tasks)
            console.print("\n🔄 [bold yellow]Starting new random cycle.[/bold yellow]\n")
            time.sleep(5)

    elif choice == "3":
        while True:
            await execute_actions(ACTIONS)
            console.print("\n🔄 [bold yellow]Repeating user-defined actions...[/bold yellow]\n")
            time.sleep(5)
    else:
        await execute_actions(ACTIONS)

asyncio.run(main())
