**Pokedex API app**

- This app exposes two API endpoints, one normal, and one with a fun translation of the data on Pokemon, i.e its name, description, habitat and legendary status.

- The code for the app is written in Python3 and is stored in the files app.py and retrieve.py.

- Prerequisites to run the code are to have Python3 installed as well as Flask server for Python installed in the system (it is added in the requirements.txt file).
**


To install Python3 on Linux(ubuntu), run the following commands or visit:

`        `sudo apt-get install software-properties-common
`           `sudo add-apt-repository ppa:deadsnakes/ppa
`           `sudo apt-get update && sudo apt-get install python3 -y

- Once python is installed, install flask using requirements.txt:
         
  `          `pip3 install -r requirements.txt

- Once the pre-requisites are installed, you will run the flask server in development mode by setting the environment variable as follows:
  `                    `export FLASK\_ENV=development

- Then run the flask server on port 5000 in the backdround with the command:
           
  `           `nohup python3 app.py &


- To access the endpoints from your local machine, use the URLs as follows:
             
  `          `http://localhost:5000/pokemon/<pokemon\_name>
  `              `&
  `             `http://localhost:5000/pokemon/translated/<pokemon\_name>
- Endpoint 1 description:

  Given a Pokemon’s name, the endpoint returns its name, standard Pokemon description, habitat and legendary status.

`                  `[http://localhost:5000/pokemon/<pokemon_name](http://localhost:5000/pokemon/%3cpokemon_name)>

- Endpoint 2 description:
 
  Given a Pokemon’s name, the endpoint returns translated Pokemon description and other basic info as in Endpoint 1, based on the following rules:
1. If Pokemon’s habitat is cave or it’s a legendary Pokemon, then Yoda translation (https://funtranslations.com/api/yoda) will be applied to description.
1. For all other Pokemon, Shakespeare translation (https://funtranslations.com/api/shakespeare) will be applied.
1. If translation is not possible, an added field “no\_translate” along with the standard description is returned in the response which gives the reason for the failure of translation.



`                          `[http://localhost:5000/pokemon/translated/<pokemon_name](http://localhost:5000/pokemon/translated/%3cpokemon_name)>

- If you are using Docker with dockerfile to run, you can do so by running the following commands:

  `      `docker build -t pokedex\_img .

`       `docker run -p 5000:5000 -t –name pokedex-app pokedex\_img

- If you are using the manifest to deploy in Kubernetes, you can create the deployment using the file “poke-dep.yml” and the following command:

  `                `kubectl create -f poke-dep.yml

  This deployment uses NodePort with 2 replicas, and uses the port for NodePort service as 30500. 
  To access the API endpoint, get the URL using:
  `                  `service pokedex-api-service –url




- If we are to run the server in production, I’d advise using a webserver with it and as well a message queue like RabbitMQ so that the API can be accessible simultaneously to large audience. 



