import requests, random, json, os, easygui, ctypes, time, discord
from colorama import init, Fore
init(convert=True)

clear = lambda : os.system("cls")

class Client:
    def __init__(self):
        self.tokens = open(easygui.fileopenbox(msg="Please select the txt file for your tokens")).read().split("\n")
        self.session = requests.Session()

    def RandomColor(self): 
        randcolor = random.randint(0x000000, 0xFFFFFF)
        return randcolor

    def Headers (self, token: str):
        headers = {
            "Content-Type": "application/json",
            "authorization": token,
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
        }
        return headers
    
    def spam(self, message: str, channelID: str, tts: bool, amount: int, delay: int):

        _message = {
            "content": message,
            "tts": tts,
        }
        
        for token in self.tokens:

            for _i in range(amount):
                
                time.sleep(delay)

                _data = self.session.post(f"https://discordapp.com/api/v6/channels/{channelID}/messages", json=_message, headers=self.Headers(token))

                if _data.status_code == 200:
                    print(f"[{Fore.CYAN}!!{Fore.RESET}] Sent a new message!")
                else:
                    ''

        self.start()

    def join(self, code: str):

        for token in self.tokens:

            _data = self.session.post(f"https://discordapp.com/api/v6/invites/{code}", headers=self.Headers(token)).json()

            if _data.status_code == 200:
                print(f"[{Fore.BLUE}!!{Fore.RESET}] Joined the {_data['guild']['name']} server.")
            else:
                print(f"[{Fore.RED}!!{Fore.RESET}] Could not join the guild on token: {token}")

        self.start()

    def start(self):

        if self.tokens == []:
            clear()
            print(f"[{Fore.BLUE}>{Fore.RESET}] Tokens File Selection {Fore.RESET}")
            time.sleep(1)
            self.tokens = open(easygui.fileopenbox(msg="Please select the txt file for your tokens")).read().split("\n")

        clear()
        print(f"{Fore.BLUE}[{Fore.RESET}1{Fore.BLUE}] Join Server {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}2{Fore.BLUE}] Spam channel {Fore.RESET}")
        print(f"{Fore.BLUE}[{Fore.RESET}3{Fore.BLUE}] Exit Application {Fore.RESET}")
        option = int(input("> "))

        if option not in [1,2,3]:
            print(f"[{Fore.RED}Invalid Option{Fore.RESET}]")
            time.sleep(1)
            self.start()

        if option == 1:
            clear()
            print(f"[{Fore.BLUE}>{Fore.RESET}] Server Invite {Fore.RESET}")
            code = str(input("> "))

            if "https://discord.gg/" in code:
                code = code.split("https://discord.gg/")[1]
            else:
                code = code 
            
            self.join(code)

        if option == 2:
            clear()

            print(f"[{Fore.BLUE}>{Fore.RESET}] Channel Id {Fore.RESET}")
            channelID = str(input("> "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Message Content {Fore.RESET}")
            message = str(input("> "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Amount of messages to send {Fore.RESET}")
            amount = int(input(" "))
            print(f"[{Fore.BLUE}>{Fore.RESET}] Delay (1,2,3)[seconds] {Fore.RESET}")
            delay = int(input(" "))

            self.spam(message=message, channelID=channelID, tts=False, amount=amount, delay=delay)

        if option == 3:
            clear()
            exit()
            

if __name__ == "__main__":
    Client().start()
