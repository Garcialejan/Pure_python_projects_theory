from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def welcomme():
    return "Welcome to FastAPI implementation"

@app.get("/index")
async def index():
    return "Welcome to the index page mtfk"

if __name__=="__main__":
    app.run(debug=True)
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run()