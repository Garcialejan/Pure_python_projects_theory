from fastapi import FastAPI, Request
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()

# Monta las carpetas estáticas (si tienes archivos CSS, JS, imágenes, etc.)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura Jinja2 para renderizar plantillas. Definimos el directorio en el que se encuentran
# estas plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    return "<html><H1>Welcome to the flask course</H1></html>"


#! Definir la request en FastAPI es necesario cuando quieres acceder a
#! información relacionada con la solicitud HTTP entrante, como encabezados,
#! cookies, parámetros de consulta, y otros datos relevantes.

# * Cuando utilizas Jinja2Templates para renderizar plantillas HTML, necesitas pasar
# * el objeto request como parte del contexto

@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
