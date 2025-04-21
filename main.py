from fastapi import FastAPI
from fastapi.responses import HTMLResponse
 
app = FastAPI()

@app.get("/error")
def error():
    html_content = "<h2>ERROR page</h2>"
    return HTMLResponse(content=html_content)

@app.get("/search")
def search():
    html_content = "<h2>Search page</h2>"
    return HTMLResponse(content=html_content)

@app.get("/help")
def help():
    html_content = "<h2>Help page</h2>"
    return HTMLResponse(content=html_content)

@app.get("/about")
def about():
    html_content = "<h2>About page</h2>"
    return HTMLResponse(content=html_content)

@app.get("/")
def root():
    html_content = "<h2>Overtrain! init 2</h2>"
    return HTMLResponse(content=html_content)
