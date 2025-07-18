from fastapi import FastAPI,Query,HTTPException
import json
from fastapi import Path
app= FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message":"this is patients data"}

@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/view/{id}")
def view():
    data = load_data()
    return data


@app.get("/patient/{id}")
def view_patient(id:str = Path(...,description='id of patient db',example="1",le="3")):
    #load all patients
    data = load_data()
    if id in data:
        return data[id]
    return HTTPException(status_code=404,detail="Patient not found")

@app.get("/sort")
def sort_patient(id:str = Query(...,description='sort by basis by height weight',order: str= Query('asc',description='sort in asc or desc'))):
    valid_fileds = ['height','weight']

