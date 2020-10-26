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

# Obtener un listado de todos los registros 
# de la tabla estudiantes, que tengan al menos 
# un número telefónico con la cadena “091”

# para la solución se hace uso del método 
# join aplicado a query

estudiantes = session.query(Estudiante).join(NumeroTelefonico).filter(NumeroTelefonico.numero_telefonico.like("091%")).all()

print("Consulta 1 ")
for e in estudiantes: 
    print(e) 
    for t in e.numerostelefonicos:
        print(t) 

# obtener un listado de todos los registros 
# de la tabla numerostelefonicos, que tengan 
# en su atributo numero_telefonico la 
# cadena “091”.

numeros_telefonicos = session.query(NumeroTelefonico).filter(NumeroTelefonico.numero_telefonico.like("091%")).all() 

print("Consulta 2 ")
for t in numeros_telefonicos:
    print("%s - %s" % (t, t.estudiante))

# Obtener un listado de todos los registros 
# de la tabla estudiantes y numerostelefonicos, que tengan al menos 
# un número telefónico con la cadena “091”

# para la solución se hace uso del método 
# join aplicado a query
# en el query se ubican las dos entidades involucradas
# 

estudiantes = session.query(Estudiante, NumeroTelefonico).join(NumeroTelefonico).filter(NumeroTelefonico.numero_telefonico.like("091%")).all()

print("Consulta 3 ")

for registro in estudiantes: 
    # el registro continen 
    # dos valores en un tupla
    # posición 0 el estudiante
    # posición 1 el número telefónico
    # que cumplen con la condición
    print(registro[0])
    print(registro[1])
