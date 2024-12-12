#API creada por Eric Muñoz Ledo Popoca

#Importación de elementos necesario
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

#Modelo de datos para alumno
class Alumno(BaseModel):
    boleta = int        #Numero de identificación
    nombre = str        
    edad = int
    correo = str        #Institucional  
    cursante = bool     #¿Cursa actualmente o es exalumno?

app = FastAPI()

#Para la persistencia de datos se crea el archivo JSON
DATA_FILE = "alumnos.json"

#Base de datos local
alumnos_db : List[Alumno] = []

#Carga y guardado de datos del JSON a la memoria local
#Cargar datos
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            datos = json.load(file)
            return [Alumno(**alumno) for alumno in datos]
    return []

#Guardar datos
def guardar_datos():
    with open(DATA_FILE, "w") as file:
        json.dump([alumno.dict() for alumno in alumnos_db], file, indent=4)

#Inicializar la base de datos
alumnos_db = cargar_datos()

