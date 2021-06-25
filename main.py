import random, os, requests, json, colorama, time, threading
from colorama import Fore

class Anonfiles():
    def __init__(self):
        self.chars = "abccdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.code = ""
    
    def gen_code(self):
        for i in range(10):
            self.code += random.choice(self.chars)

        self.check()
    
    def check(self):
        r = requests.get(f'https://api.anonfiles.com/v2/file/{self.code}/info').json()

        if(r['status'] == "True"):
            print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.GREEN}Working Code: {Fore.WHITE}{r['data']['file']['metadata']['id']}{Fore.RESET}  |  Name: {Fore.WHITE}{self.code}{Fore.RESET}")
            open('good_code.txt', 'a+').write(f'https://anonfiles.com/{code_id}/{name}\n')
        
        else:
            print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}Invalid Code: {Fore.WHITE}{self.code}{Fore.RESET} | Error: {r['error']['type']}")


class Console():
    def __init__(self):
        os.system('cls && title Anonfiles Cracker ^| github.com/Kanekiweb ^| discord.gg/kaneki ||clear')
        print(f"""
        
      ___                      _____                _    
     / _ \                    /  __ \              | |   
    / /_\ \_ __   ___  _ __   | /  \/_ __ __ _  ___| | __
    |  _  | '_ \ / _ \| '_ \  | |   | '__/ _` |/ __| |/ /
    | | | | | | | (_) | | | | | \__/\ | | (_| | (__|   < 
    \_| |_/_| |_|\___/|_| |_|  \____/_|  \__,_|\___|_|\_\\ \n
                                                     
        github.com/{Fore.RED}KanekiWeb{Fore.RESET} - discord.gg/{Fore.RED}kaneki{Fore.RESET}        

    """)


Console()
while True:
    threading.Thread(target=Anonfiles().gen_code()).start()