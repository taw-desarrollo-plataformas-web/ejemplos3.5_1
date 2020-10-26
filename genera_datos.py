from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

# se crea un objetos de tipo Estudiante 
estudiante1 = Estudiante(nombre="Tony", apellido="García", \
        cedula="123456789")
estudiante2 = Estudiante(nombre="Annette", apellido="García", \
        cedula="223456789")
estudiante3 = Estudiante(nombre="David", apellido="Phillips", \
        cedula="323456789")

# Se crean objeto de tipo NumeroTelefonico
# con sus propiedades
# numero_telefonico
# tipo
# adicional a cada objeto se le agrega
# un objeto de tipo Estudiante para el 
# atributo estudiante
# que representa la relación
#
telefono1 = NumeroTelefonico(numero_telefonico="0912345678", \
        tipo="personal", \
        estudiante=estudiante1)
telefono2 = NumeroTelefonico(numero_telefonico="0212345678", \
        tipo="domicilio", 
        estudiante=estudiante1)
telefono3 = NumeroTelefonico(numero_telefonico="0942345678", \
        tipo="personal", 
        estudiante=estudiante2)
telefono4 = NumeroTelefonico(numero_telefonico="0342345678", \
        tipo="domicilio", 
        estudiante=estudiante2)
telefono5 = NumeroTelefonico(numero_telefonico="0952345678", \
        tipo="personal", 
        estudiante=estudiante3)



# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos
session.add(estudiante1)
session.add(estudiante2)
session.add(estudiante3)
session.add(telefono1)
session.add(telefono2)

# se confirma las transacciones
session.commit()
