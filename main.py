from fastapi import FastAPI
import uvicorn
#uvicorn sirve para ejecutar el fastapi de python

app = FastAPI()

@app.get('/')
def message():
    return 'hola bitpro bienvenido a fastapi tu primer backend'

@app.get('/jose')
def message():
    return 'esto es about de farmacia'

@app.get('/home')
def message():
    return 'este es el home'


#como dejar de utilizar el comando de uvicorn #uvicorn main:app
#con esta linea de codigo se automatiza eso

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000)


