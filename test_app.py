from app import app

def test_add_and_update():
    client = app.test_client()
    assert client.post("/medicines", json={"name":"Paracetamol","quantity":20}).status_code == 201
    r = client.put("/medicines/Paracetamol", json={"quantity":35})
    assert r.status_code == 200
    assert r.json["medicine"]["quantity"] == 35

def test_update_missing():
    assert app.test_client().put("/medicines/Unknown", json={"quantity":4}).status_code == 404

def test_health():
    assert app.test_client().get("/health").status_code == 200