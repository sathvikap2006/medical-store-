from app import app

def test_add_update_view():
    client = app.test_client()
    assert client.post("/medicines", json={"name":"Paracetamol","quantity":20}).status_code == 201
    assert client.put("/medicines/Paracetamol", json={"quantity":35}).status_code == 200
    r = client.get("/medicines")
    assert r.status_code == 200
    assert any(x["name"] == "Paracetamol" and x["quantity"] == 35 for x in r.json)

def test_health():
    assert app.test_client().get("/health").status_code == 200
