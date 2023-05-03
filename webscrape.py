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

div_enemies = str(soup.find_all("div", id="gallery-0")).split()  

matched_enemies = list(filter(lambda v: match("^href", v), div_enemies))

reg_patterns = ['"', '^href=', r'/.+?\bFile\b.*']
comb_pats = r'|'.join(map(r'(?:{})'.format, reg_patterns))

def filt_enemies(x):
    for val in x:
        final_enemies.append(sub(comb_pats, '', val))
        if final_enemies[-1]:
            continue
        else:
            final_enemies.pop(-1)

filt_enemies(matched_enemies)
print(final_enemies)
