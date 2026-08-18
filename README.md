# Python Kubernetes & CI/CD & GitOps

End-to-end DevOps project demonstrating a Python application deployment to Kubernetes using GitHub Actions, Docker, GitOps and Argo CD.

## Architecture

```text
Developer
   │
   ▼
GitHub Application Repo
   │
   ▼
GitHub Actions
   │
   ├── Tests
   ├── Docker Build
   └── Docker Push
           │
           ▼
       Docker Hub
           │
           ▼
      GitOps Repo
           │
           ▼
        Argo CD
           │
           ▼
      Kubernetes
           │
           ▼
      Python App
```

---

## Technologies

- Python / Flask
- Pytest
- Docker
- Docker Hub
- Kubernetes
- Minikube
- GitHub Actions
- GitOps
- Argo CD

---

## Repository Structure

```text
python-app/
├── src/
├── tests/
├── Dockerfile
└── requirements.txt

.github/
└── workflows/
    └── ci.yaml


python-app-gitops/
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml

```

---

## CI/CD Flow

- Developer pushes code to main.
- GitHub Actions runs automated tests.
- Docker image is built and tagged with the Git commit SHA.
- Image is pushed to Docker Hub.
- GitHub Actions updates the Kubernetes image in the GitOps repository.
- Argo CD detects the Git change.
- Argo CD synchronizes Kubernetes with the desired state.

## GitOps

The Kubernetes manifests are maintained in a dedicated GitOps repository.

Git is the source of truth for the desired Kubernetes state, while Argo CD continuously reconciles the cluster with the repository.

## Current Kubernetes Setup

- Kubernetes cluster: Minikube
- Application: Python / Flask
- Deployment: 2 replicas
- Service: Kubernetes Service
- Ingress: NGINX Ingress
- CD: Argo CD
