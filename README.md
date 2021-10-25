# FastAPI implementation of a product recommender 

## Getting started
To use, fork and clone this repository. Then install the required packages from the command line with

`pip install -r requirements.txt` 

Create a local server with 

`uvicorn app:app --reload`

Make a test call to the server. For example, type this url in the browser "http://127.0.0.1:8000/products/112808" The three most similar products are returned. The result is a JSON object with the product id followed by the cosine similarity score. 

See your automatically created interactive API docs at http://127.0.0.1:8000/docs

Shut down the server with `ctrl` + `c`

### Tests
To create new tests `pip install pytest selenium hypothesis`

Then `pytest`

See FastAPI's testing tutorial [here](https://fastapi.tiangolo.com/tutorial/testing/)


## The recommender
Uses cosine similarity of Home Depot product descriptions to recommend similar Home Depot products. Returns the product id and similarity score of the most similar products.

## The data
The dataset is a subset of Home Depot products from Kaggle available [here](https://www.kaggle.com/c/home-depot-product-search-relevance/data).

