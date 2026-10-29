from app import app

def test_health():
    assert app.test_client().get("/health").status_code == 200

def test_add_medicine():
    r = app.test_client().post("/medicines", json={"name":"Paracetamol","quantity":20})
    assert r.status_code == 201
    assert r.json["medicine"]["quantity"] == 20

def test_reject_invalid_medicine():
    r = app.test_client().post("/medicines", json={"name":"","quantity":-1})
    assert r.status_code == 400
