def test_live(client):
    r = client.get("/api/v1/health/live")
    assert r.status_code == 200
