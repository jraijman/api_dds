from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv,dotenv_values
import os

load_dotenv()
db_connection = os.getenv("DB_CONNECTION")

print(f"DB_CONNECTION: {db_connection}") 

engine = create_engine(db_connection)

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

Base = declarative_base()

class PuntoDonacion(Base):
    __tablename__ = 'centro_donacion'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    direccion = Column(String(255), nullable=True)

# Configuración de la base de datos
engine = create_engine(db_connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)