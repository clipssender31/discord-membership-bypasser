import httpx, random, os, pyfiglet; from itertools import cycle; from concurrent.futures import ThreadPoolExecutor; from colorama import Fore, init
init(autoreset=True)



class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def bypass(tokens: str, serverid: str):
    try:
        with open("./proxies.txt") as fp:
                proxies = fp.read().splitlines()
        client = httpx.Client(timeout=30,headers={"Pragma": "no-cache", "Accept": "*/*", "Host": "discord.com", "Accept-Language": "en-US", "Cache-Control": "no-cache", "Accept-Encoding": "br, gzip, deflate", "Referer": "https://discord.com/", "Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
                                                                             "X-Track": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi11cyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy4xLjIgU2FmYXJpLzYwNS4xLjE1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMuMS4yIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEzNTQ5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, cookies={"locale": "en-US"}, proxies=f"http://{random.choice(proxies)}")
            
        client.headers["X-Fingerprint"] = client.get("https://canary.discord.com/api/v10/experiments", timeout=30).json()["fingerprint"]
        client.headers["X-Super-Properties"] = "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi11cyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy4xLjIgU2FmYXJpLzYwNS4xLjE1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMuMS4yIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTE3OTE4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        client.headers["Authorization"] = tokens
        client.headers["Origin"] = "https://discord.com"
    
        jsondata=client.get(f'https://discord.com/api/v9/guilds/{serverid}/member-verification')
        if jsondata.status_code==200:
            bypass=client.put(f'https://discord.com/api/v9/guilds/{serverid}/requests/@me', json=jsondata.json())
            if bypass.status_code==201:
                print(f"{Fore.GREEN}[+]{Fore.RESET} Token: {tokens} is bypassed")
            else:
                print(f"{Fore.RED}[!]{Fore.RESET} Received a bad response from the server: {bypass.json()}")
        else:
            print(f"{Fore.RED}[!]{Fore.RESET} Received a bad response from the server: {jsondata.json()}")
    except Exception as e:
        print(e)

def Gettokens():
    with open('./tokens.txt', 'r') as temp_file:
        token = [line.rstrip('\n') for line in temp_file]
    return token
token = Gettokens()
tokens_pool = cycle(token)

if __name__ == "__main__":
    os.system("cls")
    init(autoreset=True)
    print(pyfiglet.figlet_format("Discord Token Bypasser"))
    print(f"{Fore.GREEN}[?]{Fore.RESET} {Fore.RED}Author: clipssender#2920{Fore.RESET}")
    threadAmount=input(f'{Fore.GREEN}[+]{Fore.RESET} {Fore.RED}How many accounts do you want to bypass?: {Fore.RESET}')
    serverid2=input(f'{Fore.GREEN}[+]{Fore.RESET} {Fore.RED}What is the server ID: {Fore.RESET}')
    threadAmount = 1 if threadAmount == "" else int(threadAmount)
    os.system("cls")
    threads = []
    with ThreadPoolExecutor(max_workers=threadAmount) as joiner:  
        for x in range(threadAmount):
            joiner.submit(bypass(next(tokens_pool), serverid2))




