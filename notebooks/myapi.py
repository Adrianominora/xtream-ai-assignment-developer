from fastapi import FastAPI
from typing import Optional
from datetime import datetime
import pandas as pd
import xgboost
import json

app = FastAPI()

model = xgboost.XGBRegressor()
model.load_model('../data/state_of_the_art/xgb_opt.json')

def preprocess_data(raw_data: pd.DataFrame):
    raw_data = raw_data.loc[(raw_data.x * raw_data.y * raw_data.z != 0) & (raw_data.price > 0)] # Clean zero dimensions and negative prices
    processed_data = raw_data.copy()
    processed_data['cut'] = pd.Categorical(processed_data['cut'], categories=['Fair', 'Good', 'Very Good', 'Ideal', 'Premium'], ordered=True)
    processed_data['color'] = pd.Categorical(processed_data['color'], categories=['D', 'E', 'F', 'G', 'H', 'I', 'J'], ordered=True)
    processed_data['clarity'] = pd.Categorical(processed_data['clarity'], categories=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], ordered=True)
    return processed_data

def preprocess_input(raw_input: pd.DataFrame):
    processed_input = raw_input.copy()
    processed_input['cut'] = pd.Categorical(processed_input['cut'], categories=['Fair', 'Good', 'Very Good', 'Ideal', 'Premium'], ordered=True)
    processed_input['color'] = pd.Categorical(processed_input['color'], categories=['D', 'E', 'F', 'G', 'H', 'I', 'J'], ordered=True)
    processed_input['clarity'] = pd.Categorical(processed_input['clarity'], categories=['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], ordered=True)
    return processed_input

dataset = pd.read_csv("https://raw.githubusercontent.com/xtreamsrl/xtream-ai-assignment-engineer/main/datasets/diamonds/diamonds.csv")
dataset = preprocess_data(dataset)

@app.get("/predict")
def predict(carat: float, cut: str, color: str, clarity: str, depth: float, table: float, x: float, y: float, z: float):
    diamond = {
        "carat": carat,
        "cut": cut,
        "color": color,
        "clarity": clarity,
        "depth": depth,
        "table": table,
        "x": x,
        "y": y,
        "z": z
    }
    my_diamond = pd.DataFrame.from_dict([diamond])
    my_diamond = preprocess_input(my_diamond)
    value = round(float(model.predict(my_diamond)[0]),2)
    try:
        with open('../data/api_calls/call_log.json', 'r') as read_file:
            call_log = json.load(read_file)
    except IOError:
        call_log = []
    call_log.append({"Date-Time": datetime.now().strftime("%Y/%m/%d, %H:%M:%S"), "method": "predict", "request": diamond, "response": value})
    with open('../data/api_calls/call_log.json', 'w') as fout:
        json.dump(call_log , fout)
    return value

@app.get("/find-similar")
def find_similar(n: int, carat: float, cut: str, color: str, clarity: str, depth: Optional[float] = None, table: Optional[float] = None, x: Optional[float] = None, y: Optional[float] = None, z: Optional[float] = None):
    query = {
        "n": n,
        "carat": carat,
        "cut": cut,
        "color": color,
        "clarity": clarity
    }
    result = dataset.loc[(dataset.cut==cut) & (dataset.color==color) & (dataset.clarity==clarity)].copy()
    result['diff'] = abs(result.loc['carat'] - carat)
    result_sorted = result.sort_values(by='diff')
    response = result_sorted.drop(columns=['diff']).head(n).to_json()
    try:
        with open('../data/api_calls/call_log.json', 'r') as read_file:
            call_log = json.load(read_file)
    except IOError:
        call_log = []
    call_log.append({"Date-Time": datetime.now().strftime("%Y/%m/%d, %H:%M:%S"), "method": "find-similar", "request": query, "response": response})
    with open('../data/api_calls/call_log.json', 'w') as fout:
        json.dump(call_log , fout)
    return response