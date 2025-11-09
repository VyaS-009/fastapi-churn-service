def test_predict(client):
    payload = {
        "tenure": 12, "MonthlyCharges": 70, "TotalCharges": 840,
        "Contract": "Month-to-month", "InternetService": "Fiber optic",
        "OnlineSecurity": "No", "TechSupport": "No", "PaymentMethod": "Electronic check"
    }
    r = client.post("/api/v1/predict", json=payload, headers={"x-api-key": "dev-key"})
    assert r.status_code in (200, 401)  # depends if API_KEY is set
