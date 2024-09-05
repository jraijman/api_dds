from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from old.db_connection import SessionLocal, PuntoDonacion
from geopy.distance import geodesic
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Recomendador de donaciones API",
    description="Esta API permite a los usuarios obtener recomendaciones de puntos de donación cercanos basados en su ubicación geográfica.",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PuntoDonacionCreate(BaseModel):
    nombre: str
    lat: float
    long: float
    direccion: str

class PuntoDonacionDB(BaseModel):
    id: int
    nombre: str
    lat: float
    long: float
    direccion: str

    class Config:
        orm_mode = True


@app.get("/",include_in_schema=False , summary="Página de bienvenida", description="Muestra un mensaje de bienvenida.")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/recomendaciones/", 
         summary="Obtener recomendaciones de puntos de donación cercanos",  
         description="Retorna una lista de puntos de donación ordenada por distancia en kilómetros desde la ubicación proporcionada.",
         tags=["Recomendaciones"])
def recomendar_donaciones(
        lat: float = Query(..., ge=-90, le=90, description="Latitud de la ubicacion actual (entre -90 y 90)"),
        long: float = Query(..., ge=-180, le=180, description="Longitud de la ubicacion actual (entre -180 y 180)"),
        limit: Optional[int] = Query(5, description="Número máximo de recomendaciones a mostrar"),
        db: Session = Depends(get_db)
    ):
    puntos_donacion = db.query(PuntoDonacion).all()
    if not puntos_donacion:
        raise HTTPException(status_code=404, detail="No se encontraron puntos de donacion")

    ubicacion_usuario = (lat, long)
    recomendaciones = []
    nombres_agregados = set()

    for punto in puntos_donacion:
        if punto.nombre not in nombres_agregados:
            ubicacion_punto = (punto.lat, punto.long)
            distancia = geodesic(ubicacion_usuario, ubicacion_punto).kilometers
            recomendaciones.append({
                "nombre": punto.nombre,
                "direccion": punto.direccion,
                "ubicacion": {
                    "lat": punto.lat,
                    "long": punto.long
                },
                "distancia_km": distancia.__round__(2)
            })
            nombres_agregados.add(punto.nombre)

    # Ordenar las recomendaciones por distancia
    recomendaciones.sort(key=lambda x: x["distancia_km"])

    if limit is not None:
        recomendaciones = recomendaciones[:limit]

    return recomendaciones

@app.post("/puntos/", 
          summary="Crear nuevos puntos de donación", 
          description="Permite crear nuevos puntos de donación proporcionando nombre, latitud, longitud y dirección.",
          response_model=List[PuntoDonacionDB],
          tags=["Puntos de Donación"])
def crear_puntos_donacion(puntos: List[PuntoDonacionCreate], db: Session = Depends(get_db)):
    nuevos_puntos = []
    for punto in puntos:
        nuevo_punto = PuntoDonacion(
            nombre=punto.nombre,
            lat=punto.lat,
            long=punto.long,
            direccion=punto.direccion
        )
        db.add(nuevo_punto)
        nuevos_puntos.append(nuevo_punto)
    db.commit()
    for nuevo_punto in nuevos_puntos:
        db.refresh(nuevo_punto)
    return nuevos_puntos