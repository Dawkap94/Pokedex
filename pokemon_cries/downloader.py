import pypokedex
import requests
from bs4 import BeautifulSoup
pkmn_dex = 150
for _ in range(150, 153):
    print(pkmn_dex)
    pkmn_dex1 = str(pkmn_dex)
    pkmn_name = pypokedex.get(dex=pkmn_dex).name.capitalize()
    url = f"https://downloads.khinsider.com/game-soundtracks/album/pokemon-x-y-cries/{pkmn_dex1}%2520-%2520Kanto%2520-%2520{pkmn_name}.mp3"
    response = requests.get(url)
    bs4_page = BeautifulSoup(response.text, "html.parser")
    bs_list = [link['href'] for link in bs4_page.find_all('a', href=True)]
    link = bs_list[len(bs_list)-2]


    r = requests.get(link)

    with open(f"{pkmn_name}.mp3", "wb") as f:
        f.write(r.content)
    pkmn_dex += 1