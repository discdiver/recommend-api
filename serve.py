from compute_similar import get_cosine_df
from fastapi import FastAPI

app = FastAPI()

@app.get('products/{productid}')
async def get_similar_prods(productid: str):
    try:
        return get_cosine_df(productid)
    except Exception:
        print(
            """Sorry, there was an error. 
            Are you sure that Product ID exists?"""
        )
