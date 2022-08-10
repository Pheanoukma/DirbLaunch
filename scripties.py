

import os
import socket
import sys 
import time as t
from time import sleep
from rich.console import Console
from colorama import init, Fore, Back
init()
banner = """
  StockTool       inc , DirbLaunch
-----Please Enter the url-----


"""
print(banner)
doshost = str(input(" Enter the website for dirb'in "))
wordlist = str(input("Wordlist [yeah enter because im cool B)]"))
C = socket.gethostbyname(doshost)
banner = """
Launching attack...
"""
print(banner)
print(" Target locked on ", C)
console = Console()
tasks = [f"task {n}" for n in range(1, 5)]

with console.status("[bold green]Working on the files...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
print("File loading and initializing....x   ") 
os.system('clear')
os.system(f' sudo dirb https://+{C} {wordlist}')
print("Dirb launched.")
print(Fore.RED+"Program will terminate in 10 seconds...")
sleep(10)