# Recomendador de donaciones API

## Descripción
Esta API permite a los usuarios obtener recomendaciones de puntos de donación cercanos basados en su ubicación geográfica.

## Endpoints

### Obtener Recomendaciones de Donación

**URL:** `/recommendations/`

**Método:** `GET`

**Parámetros:**
- `lat` (float): Latitud de la ubicación actual.
- `lon` (float): Longitud de la ubicación actual.
- `limit` (int, opcional): limite de respuestas.

**Respuesta:**
- `200 OK` con una lista de puntos de donación cercanos.


## Para levantar la api de forma local
- Utiliza base de datos MySql (controlar nombre de base de datos y usuario y contraseña)
- Utilizar comando `uvicorn main:app --reload` en la consola del proyecto
