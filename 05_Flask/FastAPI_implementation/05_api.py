from fastapi import FastAPI, Request, Form, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
 

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    id: int
    name: str
    description: str
    
# Initial data in my to do list
items = [
    Item(id= 1, name= "Item 1", description= "This is item 1"),
    Item(id= 2, name= "Item 2", description= "This is item 2")
]

@app.get("/")
async def home(request: Request):
    return "Welcome to the Sample to do list APP"

# Get all the avaiable items
@app.get("/items")
async def get_items(request:Request):
    return items

## get: Retireve a specific item by Id
@app.get("/items/{item_id}", status_code=200,
         response_model=Item)
async def get_items(item_id: int, request:Request):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail = "Item not found")
    else:
        return item
    
### The same but generating a template
@app.get("/items_template/{item_id}", status_code=200,
         response_class=HTMLResponse)
async def get_items(item_id: int, request:Request):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail = "Item not found")
    else:
        return templates.TemplateResponse("item_detail.html",
                                          {"request": request,
                                           "item": item})


# Modelo para crear un nuevo Item sin especificar id (ItemCreate)
# Si usaramos la clase base (Item), sería obligatorio especificar el ID 
# a la hora de realizar la petición.
class ItemCreate(BaseModel):
    name: str
    description: str
    
## Post :create a new task- API
@app.post("/items", status_code=201, response_model=Item)
async def create_item(request:Request, item:ItemCreate):
    # Verificamos si la solicitud tiene algún campo de entrada
    if not item.name or not item.description:
        raise HTTPException(status_code=400,
                            detail="Name and description are required")

    # Crear un nuevo item
    new_item = Item(
        id=items[-1].id + 1 if items else 1,
        name=item.name,
        description=item.description
    )
    items.append(new_item)
    return new_item
    