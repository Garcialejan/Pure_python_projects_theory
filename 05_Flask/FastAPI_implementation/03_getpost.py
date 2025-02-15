from fastapi import FastAPI, Request, Form

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
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about",response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


 # Definimos un modelo de datos utilizando Pydantic para validar los datos
 # enviados en el formulario
class FormData(BaseModel):
    name: str

@app.post("/form", response_class=HTMLResponse)
async def form(name: str = Form(...)):
    return f'Hello {name}!'

@app.get("/form", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
# ! Alternativa a la definición de dos funciones diferentes
# ! para GET y POST
# @app.get("/submit", response_class=HTMLResponse)
# @app.post("/submit", response_class=HTMLResponse)
# async def submit(request: Request,
#                  science: Optional[float] = Form(None),
#                  maths: Optional[float] = Form(None), 
#                  c: Optional[float] = Form(None),
#                  datascience: Optional[float] = Form(None)):
#     if request.method == "POST":
#         pass
#     else:
#         pass

@app.post("/submit", response_class=HTMLResponse)
async def submit(name: str = Form(...)):
    return f'Hello {name}!'

# Segurar que se pasa el formulario cuando se realiza el get
@app.get("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})