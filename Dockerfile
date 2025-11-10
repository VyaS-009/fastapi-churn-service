# ---- Builder Stage ----
# This stage installs dependencies, including build-time tools.
FROM python:3.12-slim AS builder

# Set environment variables for cleaner builds and logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Install build dependencies needed for some Python packages
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt


# ---- Final App Stage ----
# This stage creates the final, lean image for production.
FROM python:3.12-slim AS app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install curl for the healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Copy installed packages from the builder stage
COPY --from=builder /usr/local/lib/ /usr/local/lib/
# Copy executables (like uvicorn) from the builder stage
COPY --from=builder /usr/local/bin /usr/local/bin
# Copy application code
COPY ./app /app/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
