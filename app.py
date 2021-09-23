from flask import Flask, json, request
from retrieve import *

api = Flask(__name__)

@api.route('/pokemon/<name>', methods=["GET"])
def getPokemon(name):
    name = name.lower()
    data = getData(name)#getData() function gets the details on the Pokemon using PokéApi (https://pokeapi.co/)
    return json.dumps(data, ensure_ascii=False, indent=4)#ascii is set to false so as to preserve the original description

@api.route('/pokemon/translated/<name>', methods=["GET"])
def getPokemonTranslated(name):
    name = name.lower()
    data = getData(name, translate=True)#getData() accepts value of translate, default is False. Uses https://funtranslations.com/ API to translate
    return json.dumps(data, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    api.run(host='0.0.0.0')

