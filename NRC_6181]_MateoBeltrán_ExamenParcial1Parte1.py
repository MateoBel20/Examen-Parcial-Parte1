'''
El personal académico de  una institución es la clase
madre del presente programa, la cual tiene como atributos
nombre, apellido y edad.
La clase hija, la cual es docente, tiene como atributos 
el rol, el departamento y su salario.
En este programa se implementa dos métodos ("registra y mostrar")
los cuales se encargan de registrar a los docentes y muestra la informción
respectivamente.
Las variables a utilizar son las siguientes:
nombre,apellido,edad,rol,departamento y salario, de las cuales
solo la última tiene como tipo de dato entero 
'''

#Clase madre
class PersonalAcademico:
    #Método constructor
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
#Clase hija
class Docente(PersonalAcademico):
    def __init__(self,rol,departamento,salario):
        self.rol=rol
        self.departamento=departamento
        self.salario=salario
#Método registrar
    def registrar(self):
        print("El docente ingresado es: ", self.nombre)
        print("Su departamento es: ",self.apellido)
        print("Su salario es: ", self.edad)
#Método mostrar
    def mostrar(self):
        print("Trabaja en el departamento de administración")

docente1=PersonalAcademico("Luis", "Ruiz", 18)

