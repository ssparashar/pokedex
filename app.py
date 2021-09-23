from flask import Flask, json, request
from retrieve import *

api = Flask(__name__)

@api.route('/pokemon/<name>', methods=["GET"])
def getPokemon(name):
    data = getData(name)
    return json.dumps(data, indent=4)

@api.route('/pokemon/translated/<name>', methods=["GET"])
def getPokemonTranslated(name):
    data = getData(name, translate=True)
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    api.run(host='0.0.0.0')

