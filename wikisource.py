# Operations reagarding fetching the poems from Wikisource
import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://pt.wikisource.org/wiki/Anexo:Sonetos_de_Bocage_em_Poesias_eroticas,_burlescas_e_satyricas_(1900)'
wiki_base_url = 'https://pt.wikisource.org'

def getPoemsList():
    r = requests.get(base_url)
    html_r = r.content
    soup = BeautifulSoup(html_r, 'html.parser')
    table = soup.find("table", class_="prettybluetable sortable")
    
    poems_titles = []
    for poem in table.find_all("a", class_="mw-redirect"):
        poems_titles.append(poem.get('title'))

    msg = ""
    for i in range(len(poems_titles)):
        msg = msg + str(i+1) + '\n' + poems_titles[i] + '\n\n'
    
    return msg

def getPoem(ind):
    r = requests.get(base_url)
    html_r = r.content
    soup = BeautifulSoup(html_r, 'html.parser')
    table = soup.find("table", class_="prettybluetable sortable")
    #poems = table.find_all("a", class_="mw-redirect")
    result = table.find("td", text=re.compile(ind)).find_next("td")
    title = table.find("td", text=re.compile(ind)).find_next("td").find_next("td")
    links = []
    for link in result.find_all('a'):
        links.append(link.get('href'))
    r = requests.get(wiki_base_url + links[0])
    html_r = r.content
    soup = BeautifulSoup(html_r, 'html.parser')
    poem = soup.find("p")
    msg = title.text + '\n' + poem.text
    return msg