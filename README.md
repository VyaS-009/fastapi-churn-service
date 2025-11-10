# 🚀 FastAPI Churn Prediction Service  
### 🧠 Production-Ready Machine Learning API with Monitoring, Docker, and Metrics

> A real-world FastAPI deployment for serving ML models — complete with **model serialization, monitoring, observability, and reproducibility**.  
> Designed as part of a production-grade **MLOps deployment series** (Day 20–21).

---

## 📖 Overview

This repository contains a **fully functional ML inference service** for **churn prediction** built using:

- ⚡ **FastAPI** — high-performance API for inference  
- 🧠 **Scikit-learn** — RandomForestClassifier trained on SaaS churn dataset  
- 🧩 **Prometheus + Grafana** — for monitoring API health, metrics, and model activity  
- 🐳 **Docker + Docker Compose** — for reproducible production builds  
- 🧰 **Makefile & .env** — for simple local automation  

This project represents a **realistic, end-to-end production ML deployment**:
From model training → serialization → FastAPI service → monitoring dashboard.

---

## ⚙️ System Architecture

```text
                        ┌──────────────────────────┐
                        │        User / Client     │
                        │  (Frontend / API call)   │
                        └────────────┬─────────────┘
                                     │
                                     ▼
                        ┌──────────────────────────┐
                        │     FastAPI Service      │
                        │--------------------------│
                        │ app/main.py              │
                        │  ├─ /api/v1/predict      │◄── Receives JSON input
                        │  ├─ /metrics             │◄── Exposes Prometheus metrics
                        │  ├─ /api/v1/health/live  │◄── Health checks for Docker
                        │  └─ /api/v1/health/ready │
                        └────────────┬─────────────┘
                                     │
                                     ▼
             ┌────────────────────────────────────────────┐
             │               Model Layer                  │
             │---------------------------------------------│
             │ models/random_forest_tuned.pkl              │
             │ models/scaler.pkl                           │
             │ models/X_columns.pkl                        │
             │---------------------------------------------│
             │   ▫ Preprocessing (StandardScaler, OneHot)  │
             │   ▫ Prediction (RandomForestClassifier)     │
             │   ▫ Confidence (predict_proba)              │
             └────────────────────────────────────────────┘
                                     │
                                     ▼
                 ┌─────────────────────────────────────┐
                 │       Prometheus (Monitoring)       │
                 │-------------------------------------│
                 │ Scrapes: /api/v1/metrics            │
                 │ Every 5 seconds                     │
                 │ Stores time-series metrics:         │
                 │   - predictions_total               │
                 │   - prediction_errors_total         │
                 │   - request duration                │
                 └─────────────────────────────────────┘
                                     │
                                     ▼
                 ┌─────────────────────────────────────┐
                 │          Grafana (Dashboards)       │
                 │-------------------------------------│
                 │ Connected to Prometheus             │
                 │ Visualizes:                         │
                 │   - API uptime (health checks)      │
                 │   - Prediction rate                 │
                 │   - Errors / Response time trends   │
                 │   - Model activity dashboard        │
                 └─────────────────────────────────────┘
````

---

## 🧰 6️⃣ DevOps Components Recap

| Component              | Purpose                                 | Notes                                                         |
| ---------------------- | --------------------------------------- | ------------------------------------------------------------- |
| **Dockerfile**         | Builds reproducible API image           | Multi-stage build (builder + final)                           |
| **docker-compose.yml** | Orchestrates API + Prometheus + Grafana | Includes healthchecks and mounted volumes                     |
| **Prometheus**         | Metric collection & scraping            | 5s scrape interval                                            |
| **Grafana**            | Visualization dashboards                | Connects via [http://prometheus:9090](http://prometheus:9090) |
| **FastAPI**            | Model inference API                     | Exposes `/predict`, `/health`, `/metrics`                     |
| **.env**               | Secrets & environment configuration     | Includes MODEL paths, API_KEY, ENV                            |
| **Makefile**           | Developer automation                    | `make run`, `make test`, `make docker`, `make monitor`        |
| **Tests**              | Local pytest integration                | Ensures endpoints respond correctly                           |

---

## 🏗️ Project Structure

```text
fastapi-churn-service/
├── app/
│   ├── api/
│   │   ├── routers/
│   │   │   ├── predict.py
│   │   │   ├── health.py
│   │   │   └── metrics.py
│   │   └── errors.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── security.py
│   ├── infra/
│   │   ├── model_loader.py
│   │   ├── preprocessing.py
│   │   └── model_registry.py
│   ├── schemas/
│   │   └── churn.py
│   ├── main.py
│   └── __init__.py
├── models/
│   ├── random_forest_tuned.pkl
│   ├── scaler.pkl
│   └── X_columns.pkl
├── tests/
│   ├── test_health.py
│   └── test_predict.py
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## 🧠 Tech Stack

| Layer                | Technology                | Description                                 |
| -------------------- | ------------------------- | ------------------------------------------- |
| **API Framework**    | FastAPI                   | High-performance async API framework        |
| **Model Runtime**    | scikit-learn              | RandomForestClassifier for churn prediction |
| **Serialization**    | joblib                    | Saves and loads trained models              |
| **Preprocessing**    | pandas, numpy             | Data preparation & transformation           |
| **Monitoring**       | Prometheus, Grafana       | Metric scraping + visualization             |
| **Containerization** | Docker, Docker Compose    | Portable deployment                         |
| **Configuration**    | dotenv, Pydantic Settings | Environment-based configuration             |
| **Testing**          | pytest, requests          | Automated API testing                       |

---

## ⚡ Quickstart — Local Development

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<yourusername>/fastapi-churn-service.git
cd fastapi-churn-service
```

### 2️⃣ Setup Environment

```bash
cp .env.example .env
```

### 3️⃣ Verify Model Artifacts

Ensure the following exist in the `models/` directory:

```
models/random_forest_tuned.pkl
models/scaler.pkl
models/X_columns.pkl
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Locally

```bash
make run
```

### 6️⃣ Test API

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
-H "Content-Type: application/json" \
-H "x-api-key: dev-key" \
-d '{
  "tenure": 12,
  "MonthlyCharges": 70,
  "TotalCharges": 840,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "TechSupport": "No",
  "PaymentMethod": "Electronic check"
}'
```

➡ Visit interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Deployment

### 1️⃣ Build the Container

```bash
docker build -t churn-api:latest .
```

### 2️⃣ Run the Container

```bash
docker run -p 8000:8000 --env-file .env -v ./models:/app/models:ro churn-api:latest
```

### 3️⃣ Access API

Visit [http://localhost:8000](http://localhost:8000)

---

## 📊 Monitoring with Prometheus + Grafana

You can monitor the API locally using Docker Compose.

### 🧩 docker-compose.yml (API + Prometheus + Grafana)

```yaml
version: "3.9"
services:
  api:
    build: .
    container_name: churn_api
    env_file: .env
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models:ro
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/health/live"]
      interval: 10s
      retries: 3

  prometheus:
    image: prom/prometheus
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
```

### 📜 prometheus.yml

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "fastapi-churn"
    static_configs:
      - targets: ["api:8000"]
```

### 🧠 Start Monitoring Stack

```bash
docker compose up --build
```

➡ Prometheus: [http://localhost:9090](http://localhost:9090)
➡ Grafana: [http://localhost:3000](http://localhost:3000)

---

## ⚙️ Makefile Commands

| Command        | Description                                     |
| -------------- | ----------------------------------------------- |
| `make run`     | Run app locally with Uvicorn                    |
| `make docker`  | Build and run Docker container                  |
| `make monitor` | Launch Docker Compose with Prometheus + Grafana |
| `make test`    | Run pytest suite                                |

---

## 🧩 Endpoints

| Endpoint               | Method | Description                     |
| ---------------------- | ------ | ------------------------------- |
| `/api/v1/predict`      | POST   | Predict churn from JSON payload |
| `/api/v1/health/live`  | GET    | Liveness probe                  |
| `/api/v1/health/ready` | GET    | Readiness probe                 |
| `/api/v1/metrics`      | GET    | Prometheus metrics endpoint     |

---

## 🧪 Testing

### Run Tests

```bash
pytest -q
```

### Example Test Output

```
2 passed in 0.58s
```

---

## 📦 Deployment (Production)

### Gunicorn + Uvicorn Workers

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --workers 3 --bind 0.0.0.0:8000
```

### Kubernetes Setup

* Add **liveness** and **readiness** probes to deployment YAML
* Use ConfigMaps for `.env`
* Use PersistentVolume for models
* Expose `/metrics` for Prometheus scraping

---

## 🧠 Key Takeaways

* 🎯 **Model-to-API Deployment** — convert ML models into live APIs
* ⚙️ **MLOps Best Practices** — metrics, health checks, CI-ready structure
* 📊 **Observability** — Prometheus + Grafana integration for monitoring
* 🧱 **Reproducibility** — Dockerized and environment-driven setup

---

## 🧾 License

MIT License © 2025
Developed by [Vedavyas Viswanatham](https://www.linkedin.com/in/vedavyasviswanatham)

---

## 💡 Summary

> 🧩 A complete, ready-to-run **production ML inference API**
> with **FastAPI**, **Prometheus**, and **Grafana** — designed for **real-world MLOps**.
> Ideal for startups, applied ML engineers, and production deployments.


