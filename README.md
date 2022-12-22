# Jüsto Challenge

_En este repositorio encontrán una API Rest desarrollada en Python con el framework Django y Django Rest Framework, así mismo se incluye archivo Dockerfile
para el contendor de la django y Docker-compose para la orquestación de la base de datos en PostgreSQL y la web app en Django._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

_Se define el modelo hits de la siguiente forma:_

```
  name: nombre del hit.
  description: descripción del hit.
  assign_hitman: asesino asignado al hit.
  failed_mission: bandera que nos indica si la misión fue exitosa o fallida
```

_Se incluyen en el modelo hits los campos heredados de la clase BaseModel:_

```
  created_at: fecha y hora en que se creó el hit.
  updated_at: fecha y hora en que se modificó el hit.
```

_El campo failed_mission se deifne como un bool, con el fin de poder tener una bandera que nos permita saber si la misión fue completada de forma satisfactoria o no:_

_Los campos heredados, created_at y updated_at nos sirven como campos de auditoría. Con ellos, podemos identificar en que momento se ha realizado la creación y/o modificación de un hit._

_Los datos que se ven en el listado y en las búsquedas de hits son paginados y está establecido que son 10 datos que mostrará por página._

### Pre-requisitos 📋

_Es necesario tener instalados los siguiente programas para poder tener un entorno de desarrollo y hacer pruebas de forma local_

```
 - Python
 - Docker
 - Docker-compose
```

## Ejecutando el contendor con docker-compose ⚙️

_Para ejecutar nos dirigimos en la terminal al path en donde se encuentra nuestro proyecto y ejecutamos los siguientes pasos:_

```
  1. docker-compose build
```

_Este comando nos construirá los contenedores que se especificaron en el archivo docker-compose.yml, esperamos a que se termine de ejecutar el comando.
Una vez que se terminó de construir nuestro contenedor, procedemos a ejecutar el siguiente comando:_

```
  2. docker-compose up
```

_Este comando nos ayuda a levantar los contenedores, crea la conexión de red, la base de datos y ejecuta los comandos especificados en el apartado 
*command* del archivo docker-compose.yml, estos comandos que se ejecutan sirven para crear las migraciones, migrarlas a la base de datos y levantar el servicio de Django._

### Análisis de las pruebas funcionales 🔩

_Estas pruebas nos proporcionan el buen uso de los endpoints creados para el manejo de las consultas en el proyecto_
_Se realizan pruebas para las diferentes consultas GET, POST, PUT, PATCH, DELETE_

## Construido con 🛠️

* [Django](https://docs.djangoproject.com/) - El framework web usado
* [Django Rest Framework](https://www.django-rest-framework.org/) - Contrucción de API's
* [Docker](https://www.docker.com) - Contenedor de aplicaciones

## Autor ✒️

* **Eduardo Agreda López** - *Trabajo Inicial* - [eduardoagreda](https://github.com/eduardoagreda)
