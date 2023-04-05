from fastapi import FastAPI
from rnn_logic.model import SarimaModel

app = FastAPI()

@app.get('/')
def index():
    return "hello world"

@app.get('/predict')
def predict(dep:int):
    deps = list(range(1,96))
    deps.remove(20)
    if dep not in deps:
        return "404"
    # load le model du dep
    model = SarimaModel(dep)
    # model.predict sur le data[dep]
    predictions = model.predict()
    #return les 12 mois
    return predictions
