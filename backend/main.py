from fastapi import FastAPI



aplication = FastAPI()



@aplication.get('/')
def prueba():
    return{'hola': 'Hello word'}