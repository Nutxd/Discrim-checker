import requests
import colorama
from colorama import Fore,init
init()


tokens = []
def load_token():
    with open('check.txt', 'r') as f:   
        for x in f.readlines():
            tokens.append(x.replace('\n',''))

def checker():
    for x in tokens:
        api = 'https://discordapp.com/api/users/@me'
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Authorization":x,
            "Content-Type":"application/json"
        }
        r = requests.get(api,headers=headers)
        discrim = r.json()['discriminator']
        print(Fore.YELLOW+x+"|#"+discrim)
        with open("discrims.txt", "a") as save:
            save.write(x+"|#"+discrim+"\n")

load_token()
checker()
