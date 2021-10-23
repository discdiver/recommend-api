import pandas as pd
from fastapi import FastAPI



cos_df = pd.read_pickle('similarities.pkl')

app = FastAPI()

@app.get('/products/{productid}')
async def get_similar_prods(productid: int):
    try:
        
        top3 = cos_df.loc[:, 111633].nlargest(4)[1:]
        return top3
    except Exception:
        print(
            """Sorry, there was an error. {Exception}
            Are you sure that Product ID exists?"""
        )

# TODO add logging
# TODO add product text
# TODO require product names to be a max length