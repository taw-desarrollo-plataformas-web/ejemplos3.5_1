from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Estudiante, NumeroTelefonico

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad estudiantes (clase Estudiante) 
estudiantes = session.query(Estudiante).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Estudiantes")
for s in estudiantes:
    print("%s" % (s))
    # desde cada objeto de la lista
    # estudiantes
    # se puede acceder a sus número telefónicos
    # haciendo uso de la relación
    # Importante
    # s.numerostelefonicos es un lista de
    # número telefónicos
    # Se hace uso de un ciclo repetitivo para
    # la presentación
    for t in s.numerostelefonicos:
        print("\t%s" % (t) )
    print("---------")



