# Aplicación Rest-API 

Api que utiliza flask para acceder a dos recursos

## Getting Started

Permite utilizando mongodb acceder a datos utilizando una api

### Prerequisites


```
mongoDB
virtualenv

```

### Installing

Generar el archivo de configuración de la aplicación


```
cp app/config.ini.template app/config.ini
```

Crear ambiente de la aplicación


```
mkvirtualenv rest-api
```

Instalar aplicación


```
python setup.py install
```

Inicializar la Base de datos


```
python manage.py init_db
```

Correr aplicación sin gunicorn


```
sh run.sh
```

## Adicionales

Configuraciones adicionales en caso de ser necesarias


### Nginx

Archivo de configuración para nginx

```
server {
  listen   80;
  server_name  api-rest.domain.com;
  access_log  /var/log/nginx/api-rest.domain.com.access.log;
  error_log  /var/log/nginx/api-rest.domain.com.error.log notice;
  rewrite_log on;
  index index.php index.html;

  location / {
     client_max_body_size 50M;
     proxy_pass http://localhost:7000;
  }
  location /static/ {
      root /var/www/api-rest.domain.com/app;
      autoindex off;
  }

}

```
## Operations 

GET
'''
curl --request GET http://<ip>:<port>/api/task/<objectid>/ --header "Content-Type:application/json"
curl --request GET http://<ip>:<port>/api/task/ --header "Content-Type:application/json"
'''

PUT
'''
curl --request PUT http://<ip>:<port>/api/task/<objectid>/ --header "Content-Type:application/json" --data '{"title": "cleaner", "description": "clean the clothes"}'
'''

PATCH
'''
curl --request PATCH http://<ip>:<port>/api/task/<objectid>/ --header "Content-Type:application/json" --data '{"title": "cleaner"}'
'''

POST
'''
curl --request POST http://<ip>:<port>/api/task/ --header "Content-Type:application/json" --data '{"title": "cleaner", "description": "clean the clothes"}'
'''

DELETE
'''
curl --request DELETE http://<ip>:<port>/api/task/<objectid>/ --header "Content-Type:application/json"
'''

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```



## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
