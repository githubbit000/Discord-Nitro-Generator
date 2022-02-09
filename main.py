# random discord nitro code generator
# discord nitro code is 19 characters long

import random
import string
import requests
from colorama import Fore as c

def main():
    # generate random string
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(19))
    # check if code is valid using requests
    if requests.get('https://discord.com/api/v6/entitlements/gift-codes/' + code + '/redeem', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}).status_code == 200:
        print(f'{c.GREEN}Valid code: {code}{c.RESET}')
    else:
        print(f'{c.RED}Invalid code: {code}{c.RESET}')
        
while True:
	main()