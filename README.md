# FastAPI implementation of a product recommender 

Uses cosine similarity of Home Depot product descriptions to recommend similar Home Depot products. Returns the product id and similarity score of the most similar products.

Dataset is a subset of Home Depot products from Kaggle available [here](https://www.kaggle.com/c/home-depot-product-search-relevance/data).

To use, fork and clone.

Then install the required packages with

`pip install -r requirements.txt` 

Create a server locally with 

`uvicorn app:app --reload`


To create new tests `pip install pytest selenium hypothesis`

Then `pytest`

See FastAPI's testing tutorial [here](https://fastapi.tiangolo.com/tutorial/testing/)