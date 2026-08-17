# Python Kubernetes CI/CD & GitOps

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

---

## Repository Structure

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

---



```
