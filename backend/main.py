from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to this notes api :)"