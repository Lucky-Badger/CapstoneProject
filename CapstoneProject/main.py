from typing import Union

from fastapi import FastAPI

from FeatureModules.Services import createAccountService

app = FastAPI()

@app.get("createaccount")
def read_root():
    createAccountService()


    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#uvicorn main:app --reload
