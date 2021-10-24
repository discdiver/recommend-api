from fastapi.testclient import TestClient
from app import app, get_similar_prods

client = TestClient(app)

# def productid_should_notify_if_negative():
#     with pytest.raises() as err:
#         get_similar_prods(-101)
#     assert err == """
#     Sorry, there was an error. {Exception}
#     Are you sure that Product ID exists?
#     """

def test_server_returns_200_on_success():
    response = client.get("/products/103487")
    assert response.status_code == 200
    assert "112808" in response.json() 

def test_string_returns_integer_msg():
    response = client.get("/products/weedwacker").json()
    assert response['detail'][0]['msg'] == 'value is not a valid integer'