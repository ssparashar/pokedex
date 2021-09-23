import unicodedata
import json
import requests
from urllib.request import urlopen


r = requests.get('https://pokeapi.co/api/v2/pokemon-species/crobat/')

#with urlopen("https://pokeapi.co/api/v2/pokemon-species/jigglypuff/") as response:
#    source = response.read()

r_dict = r.json()

pokemon = dict()
pokemon['name'] = r_dict['name']
pokemon['description'] = r_dict['flavor_text_entries'][1]['flavor_text'].replace("\n", " ").replace("\x0c", " ")
pokemon['habitat'] = r_dict['habitat']['name']
pokemon['is_legendary'] = r_dict['is_legendary']

print(pokemon)
n =  r_dict['flavor_text_entries'][1]['flavor_text'].replace("\n", " ").replace("\x0c", " ")

f = json.dumps(pokemon, indent =4)

print(f)
j= {'text':n}
#n = " ".join(char for char in n if unicodedata.category(char)[0]!="C")

print(n)
print(r_dict['habitat']['name'])
#print(type(n))
#print(j)


if r_dict['habitat']['name'] == "cave" or r_dict['is_legendary'] == True:
    res = requests.post('https://api.funtranslations.com/translate/yoda.json', data=j)
    fin = res.json()
    print(res.status_code)
    #print("\n")
    #print(fin)
    print(fin['contents']['translated'])

else:
    res = requests.post('https://api.funtranslations.com/translate/shakespeare.json', data=j)
    fin = res.json()
    print("\n")
    #print(fin)
    print(fin['contents']['translated'])
