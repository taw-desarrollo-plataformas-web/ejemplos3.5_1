from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_datos
from genera_tablas import Saludo

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase2.db')

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Saludo

saludo1 = Saludo()
saludo1.mensaje = "Hola que tal"
saludo1.tipo = "informal"

saludo2 = Saludo()
saludo2.mensaje = "Buenos días"
saludo2.tipo = "formal"

saludo3 = Saludo()
saludo3.mensaje = "Que hay"
saludo3.tipo= "informal"

saludo4 = Saludo()
saludo4.mensaje = "Buenas noches"
saludo4.tipo = "formal"

# se agrega los objetos de tipo Saludo
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos demobase2.db
session.add(saludo1)
session.add(saludo2)
session.add(saludo3)
session.add(saludo4)

# se confirma las transacciones
session.commit()
