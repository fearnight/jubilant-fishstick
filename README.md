# Infrastructure & Observability Practice Project

This repository is a practice exercise designed to provision a complete containerized infrastructure, including a web application, a database, and a full observability stack, all automated via CI/CD.

## Architecture & Components

### 1. Application Stack
* **Web Application:** A simple HTML interface served via a Python script.
* **Database:** A Redis database used to track and count website visits.
* **Containerization:** Both the application and database are containerized using custom `Dockerfile`s and managed via `docker-compose`.

### 2. Observability Stack
* **Node Exporter:** Installed inside the container environment to collect system metrics (CPU usage, memory, etc.).
* **Prometheus:** Gathers and stores metrics scraped from Node Exporter.
* **Grafana:** Connects to Prometheus to visualize metrics through user-friendly dashboards.

### 3. CI/CD Pipeline (GitHub Actions)
* **Validation:** Automatically checks the validity of the `docker-compose` file and Docker images on every push/PR.
* **Build & Push:** Automatically builds the Docker image and pushes it to Docker Hub upon successful validation.
