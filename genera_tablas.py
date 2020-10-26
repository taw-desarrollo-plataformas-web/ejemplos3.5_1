from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Estudiante(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    cedula = Column(String, nullable=False)
    
    def __repr__(self):
        return "Estudiante: nombre=%s apellido=%s cedula=%s" % (
                          self.nombre, 
                          self.apellido, 
                          self.cedula)

class NumeroTelefonico(Base):
    __tablename__ = 'numerotelefonicos'
    id = Column(Integer, primary_key=True)
    numero_telefonico = Column(String, nullable=False)
    tipo = Column(String)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    estudiante  = relationship("Estudiante", back_populates="numerostelefonicos")
    
    def __repr__(self):
        return "Número Telefónico %s" % (self.numero_telefonico)

Estudiante.numerostelefonicos = relationship("NumeroTelefonico", \
        back_populates="estudiante")

Base.metadata.create_all(engine)
