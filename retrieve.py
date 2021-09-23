import json
import requests
#import json and requests module to help manipulate data by using dictionaries and to GET and POST HTTP requests

def getData(name, translate=False):
    poke_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}/"#the PokéAPI API to be used to get Pokemon(name) details
    poke_res = requests.request('GET', poke_url)#saving the PokéAPI response
    
    if poke_res.status_code != 200:
        if poke_res.status_code == 404: #error handling in case the name of Pokémon used is wrong
            return "What do we have here? Are you sure you have not discovered a new Pokémon!! If not, make sure you are spelling the name correctly."
        else:
            return f"There was a problem retrieving data: {poke_res.text}"
    else:
        poke_res_dict = poke_res.json()
        pokemon = dict() #dictionary to store the relevant details of the Pokémon fetched using the PokéAPI
        
        pokemon['name'] = poke_res_dict['name'] #name of the Pokémon
        pokemon['description'] = fetchDesc(poke_res_dict) #description of the Pokémon
        
        if poke_res_dict['habitat'] == None : #some Pokémon might have the habitat as null, exception handling in such case
            pokemon['habitat'] = "This Pokémon does not have a habitat"
        else:
            pokemon['habitat'] = poke_res_dict['habitat']['name'] #habitat of the Pokémon
        
        pokemon['is_legendary'] = poke_res_dict['is_legendary'] #legendary status of the Pokémon

        if translate == True : #in case the /translate API is called
            translate_text = {'text':pokemon['description']} #the description formatted to suit the funtranslations API format

            yoda = "https://api.funtranslations.com/translate/yoda.json" #Yoda translation API 
            shakespeare = "https://api.funtranslations.com/translate/shakespeare.json" #Shakespeare translation API

            if pokemon['habitat'] == "cave" or pokemon['is_legendary'] == True: #conditon as per habitat being cave or Pokémon being legendary
                translate_url = yoda
            else :
                translate_url = shakespeare

            translate_res = requests.post(translate_url, data=translate_text) #using the FunTranslations API to get relevant translation
            translate_res_dict = translate_res.json()
            
            if translate_res.status_code != 200:
                if translate_res.status_code == 429 and translate_url == yoda : #as on free plan of FunTranslations, API rate limit of 5
                    error_msg = truncError(translate_res_dict)
                    pokemon['no_translate'] = "Apologies, accept, become too tired to translate now, Yoda has. " + error_msg
                    return pokemon
                elif translate_res.status_code == 429 and translate_url == shakespeare :
                    error_msg = truncError(translate_res_dict)
                    pokemon['no_translate'] = "Accept apologies, Shakespeare hath becometh too did tire to translate anon. " + error_msg
                    return pokemon
            else:
                pokemon['description'] = translate_res_dict['contents']['translated'] #return the translated description
                return pokemon #return the Pokémon data with translated description
        else:
            return pokemon #return the Pokémon data when normal API is called

def fetchDesc(r_dict): #function to fetch the description in English and format the received description to a readable format
    for k in r_dict['flavor_text_entries']:
        if k['language']['name'] == "en":
            val = r_dict['flavor_text_entries'].index(k)
    return r_dict['flavor_text_entries'][val]['flavor_text'].replace("\n", " ").replace("\x0c", " ")


def truncError(t_dict): #function to truncate the rate limiting error message
    result = t_dict['error']['message'].replace("Too Many Requests: Rate limit of 5 requests per hour exceeded. ", "")
    return result


