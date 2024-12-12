# API creada por Eric Muñoz Ledo Popoca #

#Importación de elementos necesario
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

# Modelo de datos para alumno #
class Alumno(BaseModel):
    boleta: int        #Numero de identificación
    nombre: str        
    edad: int
    correo: str        #Institucional  
    cursante: bool     #¿Cursa actualmente o es exalumno?

# Crear aplicación #
app = FastAPI()

# Para el guardado de datos se crea el archivo JSON, de otra forma los datos se borran cuando se cierre el programa #
DATA_FILE = "alumnos.json"

# Base de datos local #
alumnos_db : List[Alumno] = []

# Carga y guardado de datos del JSON a la memoria local #
# Cargar datos #
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            datos = json.load(file)
            return [Alumno(**alumno) for alumno in datos]
    return []

# Guardar datos #
def guardar_datos():
    with open(DATA_FILE, "w") as file:
        json.dump([alumno.dict() for alumno in alumnos_db], file, indent=4)

# Inicializar la base de datos #
alumnos_db = cargar_datos()

# Crear alumno #
@app.post("/alumnos/", response_model=Alumno)
def crear_alumno(alumno: Alumno):
    for existente in alumnos_db:                        # Verificar que la boleta no se repita #
        if existente.boleta == alumno.boleta:
            raise HTTPException(status_code=400, detail="Boleta ya existente.")
    alumnos_db.append(alumno)
    guardar_datos()                                     # Guardar datos en JSON #
    return alumno

# Get para alumnos #
@app.get("/alumnos/", response_model=List[Alumno])
def obtener_alumnos():
    return alumnos_db

# Editar información de alumno #
@app.put("/alumnos/{alumno_boleta}", response_model=Alumno)
def actualizar_alumno(alumno_boleta: int, alumno_actualizado: Alumno):
    for index, alumno in enumerate(alumnos_db):
        if alumno.boleta == alumno_boleta:
            alumnos_db[index] = alumno_actualizado
            guardar_datos()
            return alumno_actualizado
    raise HTTPException(status_code=404, detail="Alumno inexistente.")

# Eliminar alumno #
@app.delete("/alumnos/{alumno_boleta}", response_model=Alumno)
def eliminar_alumno(alumno_boleta: int):
    for index, alumno in enumerate(alumnos_db):
        if alumno.boleta == alumno_boleta:
            eliminado = alumnos_db.pop(index)
            guardar_datos()
            return eliminado
    raise HTTPException(status_code=404, detail="Alumno inexistente.")