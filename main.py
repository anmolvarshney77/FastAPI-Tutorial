from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "My name is FastAPI! Will Complete the code in the future!"}
