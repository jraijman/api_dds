# api_tp_dds

## Descripcion
Service a presentar para el tp de dds, permite obtener las recomendaciones de puntos de donacion cercanos a una ubicacion en base a su latitud y longitud

**CURSO**: martes maniana grupo 13

## Endpoints

### Obtener Recomendacion de puntos de donacion

**Método:** `GET`

**URL:** `/recommendations/?lat=&long=&limit=`

**Parámetros:**

- `lat` (float): Latitud de la ubicación actual (entre -90 y 90).
- `lon` (float): Longitud de la ubicación actual (entre -180 y 180).
- `limit` (int, opcional): limite de respuestas.

**Respuesta:**
- `200 OK` con una lista de puntos de donación cercanos.


### Cargar punto de donacion

**Método:** `POST`

**URL** `/punto/`


**JSON:**

```
[
  {
    "nombre": "string",
    "lat": 0,
    "long": 0,
    "direccion": "string"
  }
]
```

**Respuesta:**
- `200 OK` 
  
## Levantar la api con docker

### Pasos
 1 - Tener instalado [Docker](https://docs.docker.com/desktop/install/windows-install/) y tener habilitada la virtualizacion en la bios (revisar tu fabricante)

 2 - crear un `.env` con una variable `DB_CONNECTION` y la ruta con la siguiente forma: `mysql+pymysql://*dbUser*:*dbPassword*@mysql:*dbHostingPort*/*dbName*` en la carpeta py

 3 - ejecutar `docker-compose up --build` o `docker-compose build` y `docker-compose up -d` 

 3 - dirigirse a `http://127.0.0.1:8729` (se puede modificar el puerto expuesto desde el dockerfile si es necesario)

 4 - una vez finalizado se puede terminar con `docker-compose down`

 ### debugging
 - ejecutar `docker logs *id del container*`


## Levantar la api de forma local

### Pasos
- Tener instalado [MySQL](https://www.mysql.com/downloads/)
  
- crear un `.env` con una variable `DB_CONNECTION` y la ruta con la siguiente forma: `mysql+pymysql://*dbUser*:*dbPassword*@mysql:*dbHostingPort*/*dbName*` en la carpeta py
  
- Utilizar comando `uvicorn main:app --reload --port (puerto)` en la consola parados en la folder py, en caso de no incluir el flag de port por default se asignara `http://127.0.0.1:8000`

### Dependencias 
- `fastapi`
- `sqlalchemy`
-  `geopy`
-  `pydantic`
-  `dotenv`






