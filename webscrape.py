from bs4 import BeautifulSoup
import requests 
from re import match, sub 
import configparser 
import os 

final_enemies = []

parser = configparser.ConfigParser(os.environ)

parser["DEFAULTS"] = {
        "url": "https://finalfantasy.fandom.com"
    }

parser.read('configs/config.ini')

for key, value in parser["DEFAULTS"].items():
    env_var = os.environ.get(key)
    if env_var:
        parser["DEFAULTS"][key] = env_var 

soup = BeautifulSoup(requests.get(f'{parser["DEFAULTS"]["url"]}/wiki/Final_Fantasy_VII_enemies').content, "html.parser")

reg_patterns = ['"', '^href=', r'/.+?\bFile\b.*']
comb_pats = r'|'.join(map(r'(?:{})'.format, reg_patterns))

def enemy_data():
    for i in range(1):
        div_enemies = str(soup.find_all("div", id=f'gallery-{i}')).split()
        matched_enemies = list(filter(lambda v: match("^href", v), div_enemies))
        filt_enemies(matched_enemies)   
        print(final_enemies)


def filt_enemies(x):
    for val in x:
        final_enemies.append(sub(comb_pats, '', val))
        if final_enemies[-1]:
            continue
        else:
            final_enemies.pop(-1)

enemy_data()

# filter png files out maybe into seperate array 
# visit each link in array and grab important data (need to decide what data is important)
# put important data into dictionary based off name/id 

