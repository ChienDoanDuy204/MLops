from fastapi import FastAPI, UploadFile, File
import pandas as pd
from pydantic import BaseModel
app = FastAPI()
app.state.df  = None
@app.post('/upload_csv')
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    app.state.df = df
    describe = df.describe()
    return {
        'data': df.to_dict(orient='records'), # Type json object
        'describe' : describe.to_dict(orient='tight')
    }

@app.get("/get_name_column_df")
async def get_name_column_df():
    return{
        'name_cols': list(app.state.df.columns)
    }

class InfoModelKNN(BaseModel):
    n_neighbors:int
    weights :str
    metric:str

@app.post("/post_KNN_trained")
async def KNN_trained(infoModelKNN:InfoModelKNN):
    print(infoModelKNN.n_neighbors)
    return{
        "Message": " ✅Model was trained successful"
    }