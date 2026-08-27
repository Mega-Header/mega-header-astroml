# CDC Connector for AstroML (issue #626)
# Runs the Debezium CDC connector for PostgreSQL change data capture.
#
# Build:
#   docker build -f docker/cdc-connector.Dockerfile -t mega-header-astroml-cdc-connector .
#
# Run:
#   docker run -d \
#     -e DATABASE_HOSTNAME=localhost \
#     -e DATABASE_PORT=5432 \
#     -e DATABASE_USER=mega-header-astroml \
#     -e DATABASE_PASSWORD=mega-header-astroml \
#     -e DATABASE_NAME=mega-header-astroml \
#     -e KAFKA_BOOTSTRAP_SERVERS=localhost:9092 \
#     mega-header-astroml-cdc-connector

# ---- Build stage -----------------------------------------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements-lock.txt ./
RUN pip install --no-cache-dir -r requirements-lock.txt

# ---- Runtime stage ---------------------------------------------------------
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

# Health check — verifies the connector process is alive
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8083/connectors/mega-header-astroml-cdc/status || exit 1

# Default entrypoint: start the CDC ingestion service
ENTRYPOINT ["python", "-m", "mega-header-astroml.ingestion"]
CMD ["--mode", "cdc"]