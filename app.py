import pandas as pd
from fastapi import FastAPI


cos_df = pd.read_pickle('similarities.pkl')

app = FastAPI()

@app.get('/products/{productid}')
async def get_similar_prods(productid: int):
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

# TODO add tests
# TODO add product text
# TODO require product id to be a positive integer
# TODO add logging