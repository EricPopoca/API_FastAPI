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
