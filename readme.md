# Twitter Collection
Twitter collection project is an approach to collect the data and store tweets from the specified twitter handles
 
_**Status**_: It is in development state.

## Running without docker
Run this to install the dependency for the project.
```
pin install -r requirments.txt
```
Set the Twitter credentials in the environment or use secrets directory file to set the secrets.
_*Do not commit the credentials in to git.*_ Format to provide the data in secrets/secrets.json
```
[{
    "twitter": {
        "API_KEY": "******************************",
        "API_SECRET_KEY": "******************************",
        "BEARER_TOKEN": "******************************",
        "ACCESS_TOKEN": "******************************",
        "ACCESS_TOKEN_SECRET": "******************************"
    },
    "reddit": {}
}]
``` 
## Running with docker
Requires docker to be installed on your system, and then running the below command from the root directory of your 
project.
```
docker-compose up --build

```
Use docker PS to get the name of the container.

```
docker ps
```

Get the container name from the above and replace here.
```
docker exec -it <container-name> bin/bash
```
Current RUN process manual
