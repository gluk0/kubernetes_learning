from fastapi import FastAPI
import os 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": f" from: {os.environ.get('ENV', 'DEFAULT_ENV')}"}

