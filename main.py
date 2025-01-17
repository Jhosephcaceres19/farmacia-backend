from fastapi import FastAPI
import uvicorn
#uvicorn sirve para ejecutar el fastapi de python

app = FastAPI()

medicamentos = [
    {
        "id":1,
        "nombre":"paracetamol",
        "cantidad":"4",
        "fecha_vencimiento":"25/10/2025"
    },
    {
        "id":2,
        "nombre":"grabol",
        "cantidad":"6",
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


#como dejar de utilizar el comando de uvicorn #uvicorn main:app
#con esta linea de codigo se automatiza eso

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000)


