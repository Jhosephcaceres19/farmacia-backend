from fastapi import FastAPI
import uvicorn
#uvicorn sirve para ejecutar el fastapi de python

app = FastAPI()

medicamentos = [
    {
        "id":1,
        "nombre":"paracetamol",
        "cantidad":6,
        "fecha_vencimiento":"25/10/2025"
    },
    {
        "id":2,
        "nombre":"grabol",
        "cantidad":6,
        "fecha_vencimiento":"15/02/2025"
    }
]

@app.get('/')
def message():
    return 'BITPRO FARMACIA!!'

@app.get('/medicamentos')
def get_medicamento():
    
    return medicamentos

@app.get('/medicamento/{id}')
def get_id_medicamento(id):
    for medicamento in medicamentos:
        if medicamento['id'] == int(id):
            return medicamento
        
    return "medicamento no encontrado"

#seleccionar por id y fecha de vencimiento || cantidad
@app.get('/medicamento/{id}/cantidad/{cantidad}')
def get_medicamento(id,cantidad):
    for medicamento in medicamentos:
        if medicamento['id']==int(id) and medicamento['cantidad']== int(cantidad):
            return medicamento
    return "usuario con fecha de vencimiento no encontrado"


#como dejar de utilizar el comando de uvicorn #uvicorn main:app
#con esta linea de codigo se automatiza eso

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000)


