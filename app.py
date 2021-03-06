import pandas as pd
from fastapi import FastAPI, Path, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


cos_df = pd.read_pickle('similarities.pkl')

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    """An html static home page"""
    return templates.TemplateResponse("index.html", {'request': request})

@app.get('/products/{productid}')
async def get_similar_prods(productid: int=Path(..., title="The ID of the product", gt=1)):
    """return the products most similar to the product id given

    Args:
        productid: the productid to find similar products with
    Returns:
        the 3 most similar products
    """
    
    try:
        return cos_df.loc[:, productid].nlargest(4)[1:]
    except Exception:
        print(
            """Sorry, there was an error. {Exception}
            Are you sure that Product ID exists?"""
        )
    
# TODO possibilities
# TODO add form to home page for querying
# TODO add product text
# TODO add logging
# TODO dockerize
# TODO add to a GCP db and use sqlmodel with
# TODO add tests with selenium for html portion
# TODO add authentication