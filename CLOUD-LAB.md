# Docker + Kubernetes Mini Lab

This folder adds a **containerization and local Kubernetes learning exercise** to the existing AI Risk Assessment Assistant. It does **not** alter the Streamlit Community Cloud deployment or imply production cloud infrastructure.

## Prerequisites
- Docker Desktop running
- For Kubernetes: `kubectl` and a local Kubernetes cluster (Docker Desktop Kubernetes or kind)

## 1. Build and run in Docker
Run these commands **from the repository root** after adding the files:

```sh
docker build -t risk-assistant:local .
docker run --rm -p 8501:8501 risk-assistant:local
```
Open http://localhost:8501 and test a risk description. Stop with Ctrl+C.

## 2. Optional: Deploy to local Kubernetes
Start Kubernetes in Docker Desktop and make sure `kubectl` points to that cluster. Ensure the cluster can access the local image. Docker Desktop's Kubernetes setup may share the local Docker image store, but with kind you need:

```sh
kind load docker-image risk-assistant:local --name <your-kind-cluster-name>
```

Then:

```sh
kubectl apply -f k8s/deployment.yaml
kubectl get pods
kubectl port-forward service/risk-assistant 8501:8501
```

Open http://localhost:8501. If pod shows `ImagePullBackOff`, your Kubernetes cluster cannot see the local image; load it into the cluster or push a tagged image to a registry and update the manifest. Do not publish private API keys or datasets.

Cleanup:
```sh
kubectl delete -f k8s/deployment.yaml
```

## Interview explanation
- Docker packages the Python code and dependencies into a reproducible container image.
- Kubernetes Deployment describes how to run the container; Service makes it reachable inside the cluster.
- Readiness/liveness probes check the Streamlit health endpoint.
- This is **local container orchestration**, not a deployed production service.
