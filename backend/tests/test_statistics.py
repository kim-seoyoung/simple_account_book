def test_monthly_stats_empty(client):
    resp = client.get("/api/statistics/monthly?year=2026&month=1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 0


def test_monthly_stats_with_data(client):
    cat_resp = client.post("/api/categories", json={"name": "식비"})
    cat_id = cat_resp.json()["id"]
    client.post("/api/expenses", json={"date": "2026-05-01", "amount": 10000, "category_id": cat_id})
    client.post("/api/expenses", json={"date": "2026-05-15", "amount": 20000, "category_id": cat_id})

    resp = client.get("/api/statistics/monthly?year=2026&month=5")
    data = resp.json()
    assert data["total"] == 30000
    assert len(data["by_category"]) == 1
    assert data["by_category"][0]["amount"] == 30000


def test_yearly_stats(client):
    client.post("/api/expenses", json={"date": "2026-01-10", "amount": 10000})
    client.post("/api/expenses", json={"date": "2026-03-10", "amount": 20000})

    resp = client.get("/api/statistics/yearly?year=2026")
    data = resp.json()
    assert data["total"] == 30000
    assert data["monthly"][0]["amount"] == 10000  # January
    assert data["monthly"][2]["amount"] == 20000  # March
