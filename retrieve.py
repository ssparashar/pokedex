import unicodedata
import json
import requests


def getData(name, translate=False):
    poke_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}/"
    poke_res = requests.request('GET', poke_url)
    if poke_res.status_code != 200:
        if poke_res.status_code == 404:
            return "There is a problem with the request URL. Make sure that it is correct"
        else:
            return f"There was a problem retrieving data: {poke_res.text}"
    else:
        poke_res_dict = poke_res.json()
        pokemon = dict()
        
        pokemon['name'] = poke_res_dict['name']
        pokemon['description'] = fetchDesc(poke_res_dict) #poke_res_dict['flavor_text_entries'][0]['flavor_text'].replace("\n", " ").replace("\x0c", " ")
        pokemon['habitat'] = poke_res_dict['habitat']['name']
        pokemon['is_legendary'] = poke_res_dict['is_legendary']

        if translate == True :
            translate_text = {'text':pokemon['description']}
            yoda = "https://api.funtranslations.com/translate/yoda.json"
            shakespeare = "https://api.funtranslations.com/translate/shakespeare.json"

            if pokemon['habitat'] == "cave" or pokemon['is_legendary'] == True:
                translate_url = yoda
            else :
                translate_url = shakespeare

            translate_res = requests.post(translate_url, data=translate_text)
            translate_res_dict = translate_res.json()
            if translate_res.status_code != 200:
                if translate_res.status_code == 429 and translate_url == yoda :
                    error_msg = translate_res_dict['error']['message'].replace("Too Many Requests: Rate limit of 5 requests per hour exceeded. ", "")
                    pokemon['no_translate'] = "Apologies,  accept,Become too tired to translate now,  yoda has. " + error_msg
                    return pokemon
                elif translate_res.status_code == 429 and translate_url == shakespeare :
                    error_msg = translate_res_dict['error']['message'].replace("Too Many Requests: Rate limit of 5 requests per hour exceeded. ", "")
                    pokemon['no_translate'] = "Shakespeare has become tired. " + error_msg
                    return pokemon
            else:
                pokemon['description'] = translate_res_dict['contents']['translated']
                return pokemon
        else:
            return pokemon

def fetchDesc(r_dict):
    for k in r_dict['flavor_text_entries']:
        if k['language']['name'] == "en":
            val = r_dict['flavor_text_entries'].index(k)
    return r_dict['flavor_text_entries'][val]['flavor_text'].replace("\n", " ").replace("\x0c", " ")




