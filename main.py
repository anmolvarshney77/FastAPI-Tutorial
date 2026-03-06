from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "My name is FastAPI! Didn't Complete this code till now!"}
