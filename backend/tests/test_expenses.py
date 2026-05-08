def test_create_expense(client):
    resp = client.post("/api/expenses", json={"date": "2026-05-01", "amount": 15000})
    assert resp.status_code == 201
    data = resp.json()
    assert data["amount"] == 15000
    assert data["date"] == "2026-05-01"


def test_create_expense_invalid_amount(client):
    resp = client.post("/api/expenses", json={"date": "2026-05-01", "amount": -100})
    assert resp.status_code == 422


def test_list_expenses(client):
    client.post("/api/expenses", json={"date": "2026-05-01", "amount": 10000})
    client.post("/api/expenses", json={"date": "2026-05-02", "amount": 20000})
    resp = client.get("/api/expenses?year=2026&month=5")
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_update_expense(client):
    resp = client.post("/api/expenses", json={"date": "2026-05-01", "amount": 10000})
    eid = resp.json()["id"]
    resp = client.put(f"/api/expenses/{eid}", json={"amount": 20000})
    assert resp.status_code == 200
    assert resp.json()["amount"] == 20000


def test_delete_expense(client):
    resp = client.post("/api/expenses", json={"date": "2026-05-01", "amount": 10000})
    eid = resp.json()["id"]
    resp = client.delete(f"/api/expenses/{eid}")
    assert resp.status_code == 204


def test_filter_by_category(client):
    cat_resp = client.post("/api/categories", json={"name": "테스트"})
    cat_id = cat_resp.json()["id"]
    client.post("/api/expenses", json={"date": "2026-05-01", "amount": 5000, "category_id": cat_id})
    client.post("/api/expenses", json={"date": "2026-05-01", "amount": 3000})
    resp = client.get(f"/api/expenses?year=2026&month=5&category_id={cat_id}")
    assert len(resp.json()) == 1
