from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a MySQL
DATABASE_URL = "mysql+pymysql://root:admin@localhost/donaciones"

Base = declarative_base()

class PuntoDonacion(Base):
    __tablename__ = 'centro_donacion'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    direccion = Column(String(255), nullable=True)

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
