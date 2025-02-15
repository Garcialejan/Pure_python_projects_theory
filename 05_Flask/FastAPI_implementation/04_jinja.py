from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


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

@app.post("/submit", response_class=HTMLResponse)
async def submit(name: str = Form(...)):
    return f'Hello {name}!'

# Segurar que se pasa el formulario cuando se realiza el get
@app.get("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


# Parámetros por el path
@app.get("/successres/{score}", response_class=HTMLResponse)
async def submit(score:float, request: Request):
    # * Dos opciones: definir las condiciones en la función
    # * sin necesidad de definirlo en las plantillas.
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp={'score':score,"res":res}
    
    return templates.TemplateResponse("result1.html",
                                      {"request": request,
                                       "results": exp})
    

# condición if en las plantillas Jinja2
@app.get("/succesif/{score}", response_class=HTMLResponse)
async def submit(score:int, request: Request):
    # * Definir las condiciones dentro de las plantillas
    # * y no en la función.
    return templates.TemplateResponse("result.html",
                                      {"request": request,
                                       "results": score})
    
#############################################################
# condición if en las plantillas Jinja2
@app.get("/fail/{score}", response_class=HTMLResponse)
async def submit(score:int, request: Request):
    return templates.TemplateResponse("result.html",
                                      {"request": request,
                                       "results": score})
    
from typing import Optional

# Recordar, cuando los datos no están en formato JSON debemos
# utilizar la clase Form
@app.get("/submit", response_class=HTMLResponse)
@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request,
                 science: Optional[float] = Form(None),
                 maths: Optional[float] = Form(None), 
                 c: Optional[float] = Form(None),
                 datascience: Optional[float] = Form(None)):
    if request.method == "POST":
        if science is None or maths is None or c is None or datascience is None:
            return templates.TemplateResponse("getresult.html",
                                              {"request": request,
                                               "error": "Todos los campos son requeridos"})
        try:
            science = float(science)
            maths = float(maths)
            c = float(c)
            datascience = float(datascience)
        except ValueError:
            return templates.TemplateResponse("getresult.html",
                                              {"request": request,
                                               "error": "Los valores deben ser números válidos"})
        
        total_score =  (science + maths + c + datascience)/4
        return RedirectResponse(url=f"/successres/{total_score}", status_code = 303)
    else:
        return templates.TemplateResponse("getresult.html", {"request": request})