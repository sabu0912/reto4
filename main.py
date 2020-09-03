# -*- coding: utf-8 -*-
from uuid import uuid4
# import os # modulo - sistema operativo
from os import getcwd, makedirs, listdir
from shutil import copy


'''class Docente:
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad'''
    
 
'''class Archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def mostrar_archivo(self):
        try:
            file = open(self.nombre_archivo, mode='r', encoding='utf-8')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if (file):
                file.close()
                print('Se visualiza el archivo')

    def Agregar_Docente(self, Docente):
        try:
            file = open(self.nombre_archivo, mode='a')
            Docente = f'{Docente.dni} - {Docente.nombre} - {Docente.edad}\n'
            file.write(Docente)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if (file):
                file.close()
                print('Se añade un docente')

Docente_1 = Docente(12345678, 'Ivonne', 35)
Docente_2 = Docente(91234567, 'Carlos', 32)
Archivo = Archivo('Docentes.txt')
Archivo.Agregar_Docente(Docente_1)
Archivo.Agregar_Docente(Docente_2)
Archivo.mostrar_archivo()'''


class Alumnos:
    def __init__(self, dni, nombre, edad, notas):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

class Archivo():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def mostrar_archivo(self):
        try:
            file = open(self.nombre_archivo, mode='r', encoding='utf-8')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if (file):
                file.close()
                print('Se visualiza el archivo Alumnos')

    def Agregar_Alumnos(self, Alumnos):
        try:
            file = open(self.nombre_archivo, mode='a')
            Alumnos = f'{Alumnos.dni} - {Alumnos.nombre} - {Alumnos.edad} - {Alumnos.notas}\n'
            file.write(Alumnos)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if (file):
                file.close()
                print('Se agrega un Alumno')

Alumno_1 = Alumnos('38974612', 'Adrian', 8, [20,16,18,14,19])
Alumno_2 = Alumnos('68123479', 'Nicolas', 7, [14,17,19,15,18])
Archivo = Archivo('Alumnos.txt')
Archivo.Agregar_Alumnos(Alumno_1)
Archivo.Agregar_Alumnos(Alumno_2)
Archivo.mostrar_archivo()

#nota menor
lista_notas_Alumno_1 = [20,16,18,14,19]
lista_desordenada = lista_notas_Alumno_1
lista_desordenada.sort()
print(f"La nota de menor a mayor del Alumno_1 es: {lista_desordenada}")

#nota mayor
lista_al_reves = lista_desordenada[::-1]
print(f"La nota de mayor a menor del Alumno_1 es : {lista_al_reves}")


#nota promedio
def sumar_lista(lista):
    suma = 0

    for numero in lista:
        suma += numero
    return suma

numeros = [20,16,18,14,19]
print(sumar_lista(numeros))

nota_promedio = (sumar_lista(numeros)) // 5
print(f'La nota promedio del Alumno_1 es: {nota_promedio}')

try:
    file = open("Alumnos.txt", mode='a')
    file.write('\n')
    file.write(f'{lista_desordenada}')
    file.write('\n')
    file.write(f'{lista_al_reves}')
    file.write('\n')
    file.write(f'{nota_promedio}')
except Exception as e:
            print(f'{str(e)}')
finally:
    if (file):
        file.close()
        print('Se agrega el reporte de notas')