# J眉sto Challenge

_En este repositorio encontr谩n una API Rest desarrollada en Python con el framework Django y Django Rest Framework, as铆 mismo se incluye archivo Dockerfile
para el contendor de la django y Docker-compose para la orquestaci贸n de la base de datos en PostgreSQL y la web app en Django._

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

_Se define el modelo hits de la siguiente forma:_

```
  name: nombre del hit.
  description: descripci贸n del hit.
  assign_hitman: asesino asignado al hit.
  failed_mission: bandera que nos indica si la misi贸n fue exitosa o fallida
```

_Se incluyen en el modelo hits los campos heredados de la clase BaseModel:_

```
  created_at: fecha y hora en que se cre贸 el hit.
  updated_at: fecha y hora en que se modific贸 el hit.
```

_El campo failed_mission se deifne como un bool, con el fin de poder tener una bandera que nos permita saber si la misi贸n fue completada de forma satisfactoria o no:_

_Los campos heredados, created_at y updated_at nos sirven como campos de auditor铆a. Con ellos, podemos identificar en que momento se ha realizado la creaci贸n y/o modificaci贸n de un hit._

_Los datos que se ven en el listado y en las b煤squedas de hits son paginados y est谩 establecido que son 10 datos que mostrar谩 por p谩gina._

### Pre-requisitos 馃搵

_Es necesario tener instalados los siguiente programas para poder tener un entorno de desarrollo y hacer pruebas de forma local_

```
 - Python
 - Docker
 - Docker-compose
```

## Ejecutando el contendor con docker-compose 鈿欙笍

_Para ejecutar nos dirigimos en la terminal al path en donde se encuentra nuestro proyecto y ejecutamos los siguientes pasos:_

```
  1. docker-compose build
```

_Este comando nos construir谩 los contenedores que se especificaron en el archivo docker-compose.yml, esperamos a que se termine de ejecutar el comando.
Una vez que se termin贸 de construir nuestro contenedor, procedemos a ejecutar el siguiente comando:_

```
  2. docker-compose up
```

_Este comando nos ayuda a levantar los contenedores, crea la conexi贸n de red, la base de datos y ejecuta los comandos especificados en el apartado 
*command* del archivo docker-compose.yml, estos comandos que se ejecutan sirven para crear las migraciones, migrarlas a la base de datos y levantar el servicio de Django._

### An谩lisis de las pruebas funcionales 馃敥

_Estas pruebas nos proporcionan el buen uso de los endpoints creados para el manejo de las consultas en el proyecto_
_Se realizan pruebas para las diferentes consultas GET, POST, PUT, PATCH, DELETE_

## Construido con 馃洜锔?

* [Django](https://docs.djangoproject.com/) - El framework web usado
* [Django Rest Framework](https://www.django-rest-framework.org/) - Contrucci贸n de API's
* [Docker](https://www.docker.com) - Contenedor de aplicaciones

## Autor 鉁掞笍

* **Eduardo Agreda L贸pez** - *Trabajo Inicial* - [eduardoagreda](https://github.com/eduardoagreda)
