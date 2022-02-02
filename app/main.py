from fastapi                 import FastAPI, Request
from fastapi.templating      import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# uvicorn src.app:api --reload --reload-dir=src

# CORS
origins = [
    'http://127.0.0.1:8000',
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# index build files
templates = Jinja2Templates(directory="app/templates") 

@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
