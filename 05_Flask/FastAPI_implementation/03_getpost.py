from fastapi import FastAPI, Request

from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


#! Cuando utilizas Jinja2Templates para renderizar plantillas HTML en FastAPI,
#! necesitas proporcionar un contexto que contenga todos los datos que la 
#! plantilla necesita para renderizarse correctamente. Este contexto se pasa 
#! como un diccionario al método TemplateResponse

# * La variable request contiene toda la información relacionada con la 
# * solicitud HTTP entrante, como encabezados, cookies, parámetros de 
# * consulta, etc. Al incluirla en el contexto, la plantilla puede acceder 
# * a esta información si es necesario

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Monta las carpetas estáticas (si tienes archivos CSS, JS, imágenes, etc.)
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.get("/index",response_class=HTMLResponse)
async def index(request: Request):
    return templates.get_template("index.html", {"request": request})

@app.get("/about",response_class=HTMLResponse)
async def about(request: Request):
    return templates.get_template("about.html", {"request": request})


 # Definimos un modelo de datos utilizando Pydantic para validar los datos
 # enviados en el formulario
class FormData(BaseModel):
    name: str

@app.post("/form", response_class=HTMLResponse)
async def form(request:Request, form_data: FormData):
    name = form_data.name
    return f'Hello {name}!'


@app.get("/form", response_class=HTMLResponse)
async def form(request: Request):
    return templates.get_template("form.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit(request:Request, form_data: FormData):
    name = form_data.name
    return f'Hello {name}!'

@app.get("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.get_template("form.html", {"request": request})