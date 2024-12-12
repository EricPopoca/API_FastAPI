# API_FastAPI
Muñoz Ledo Popoca Eric
API creada en FASTAPI, taller de Tecnologías Disruptivas

## Crear un entorno virtual
En terminal:
- python -m venv fa_venv

## Iniciar entorno virtual
Visual Code la mayoría de veces muestra un mensaje que permite que se cambie automaticamente; si ese no fuese el caso, en terminal:
- fa_venv/Scripts/activate.bat                      Para mensaje del sistema
- fa_venv/Scripts/Activate.ps1                      Para Powershell

## Instalar fastapi y uvicorn
En terminal:
- python -m pip install fastapi
- python -m pip install uvicorn

## Para correr el programa
En terminal:
- uvicorn Alumnos:app --reload

Esto mostrará un link que llevara al sitio, este no tiene nada en el endpoint inicial, pero si se le agrega "/docs" se puede ver la documentación con los procesos completos, así como utilizarlos