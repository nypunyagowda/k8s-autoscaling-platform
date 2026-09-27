
# Kubernetes Auto-Scaling and Self-Healing Platform

A cloud-native application deployed on Kubernetes that demonstrates **Horizontal Pod Autoscaling (HPA)** and **automatic pod recovery**. The project uses Docker and Minikube to simulate a Kubernetes environment locally.

## Overview

This project deploys a containerized Python web application on a Kubernetes cluster. It automatically adjusts the number of application replicas based on CPU utilization and replaces failed or deleted pods to maintain the desired number of replicas.

The objective is to understand core cloud-native concepts such as containerization, orchestration, resource management, health monitoring, auto-scaling, and self-healing.

## Features

- **Containerization:** Packages the Python application using Docker.
- **Kubernetes Deployment:** Manages application replicas and ensures the desired state.
- **Horizontal Pod Autoscaling:** Scales the number of replicas based on CPU utilization.
- **Self-Healing:** Automatically replaces deleted pods.
- **Health Checks:** Uses readiness and liveness probes to monitor application health.
- **Resource Management:** Defines CPU and memory requests and limits.

## Tech Stack

- Python
- Docker
- Kubernetes
- Minikube
- kubectl
- YAML
- Kubernetes Metrics Server

## Architecture

```text
             Python Application
                     |
                  Docker
                     |
             Container Image
                     |
                  Minikube
              Kubernetes Cluster
                     |
              Deployment (2+)
                     |
                  Service
                     |
            Incoming Application
                  Requests

          CPU Metrics from Metrics Server
                     |
          Horizontal Pod Autoscaler
                     |
          Adjusts Number of Replicas
```

## Project Structure

```text
k8s-autoscaling-platform/
├── app.py
├── Dockerfile
└── k8s/
    ├── deployment.yaml
    ├── service.yaml
    └── hpa.yaml
```

## Prerequisites

Install the following tools:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

The commands below are intended for Windows PowerShell.

## Setup and Deployment

### 1. Start the Kubernetes Cluster

Start Docker Desktop, then run:

```powershell
minikube start --driver=docker --cpus=4 --memory=4096
```

Enable the Metrics Server:

```powershell
minikube addons enable metrics-server
```

Verify that the cluster is running:

```powershell
kubectl get nodes
kubectl top nodes
```

### 2. Build the Docker Image

From the project root directory, build the application image:

```powershell
docker build -t k8s-autoscaling-demo:v1 .
```

Load the image into Minikube:

```powershell
minikube image load k8s-autoscaling-demo:v1
```

### 3. Deploy the Application

Apply the Kubernetes Deployment and Service:

```powershell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check the deployment and pods:

```powershell
kubectl get deployments
kubectl get pods
kubectl get services
```

### 4. Configure Auto-Scaling

Apply the Horizontal Pod Autoscaler:

```powershell
kubectl apply -f k8s/hpa.yaml
```

Check the HPA status:

```powershell
kubectl get hpa
kubectl describe hpa autoscaling-hpa
```

The HPA is configured with:

| Setting | Value |
|---|---|
| Minimum replicas | 2 |
| Maximum replicas | 6 |
| Target CPU utilization | 50% |

### 5. Access the Application

Run:

```powershell
minikube service autoscaling-service --url
```

Open the URL returned by Minikube in your browser.

## Testing and Results

### 1. Horizontal Pod Autoscaling

Generated application load to increase CPU utilization and monitored the HPA:

```powershell
kubectl get hpa -w
```

In another terminal, monitor the pods:

```powershell
kubectl get pods -w
```

**Observed result:** The HPA events showed the replica count scaling up to 4 and then 6 when CPU utilization exceeded the target. As the load decreased, the replica count scaled back down.

This demonstrates Kubernetes horizontal scaling in response to workload demand.

### 2. Self-Healing

Listed the running pods:

```powershell
kubectl get pods
```

Deleted one application pod:

```powershell
kubectl delete pod <pod-name>
```

Replace `<pod-name>` with an actual pod name from the command output.

Verified the replacement:

```powershell
kubectl get pods
kubectl get deployment autoscaling-demo
```

**Observed result:** Kubernetes automatically created a replacement pod, and the Deployment returned to its desired replica count of two.

This demonstrates Kubernetes self-healing through reconciliation of the desired state.

## Key Learnings

- Containerizing applications with Docker.
- Deploying and managing workloads using Kubernetes.
- Configuring Kubernetes Deployments, Services, and HPA.
- Understanding CPU requests, limits, and utilization metrics.
- Implementing health checks using Kubernetes probes.
- Observing automatic scaling and pod recovery.
- Running a local Kubernetes cluster using Minikube.

## Future Enhancements

- Deploy the application to a managed cloud Kubernetes service such as Amazon EKS.
- Add monitoring and visualization using Prometheus and Grafana.
- Configure CI/CD automation using Jenkins or GitHub Actions.
- Add ingress and HTTPS support.
- Improve load testing and collect scaling performance metrics.

## Author

**K S NYPUNYA**

MCA Student | Cloud Computing | Kubernetes | Docker | Python

## License

This project is available for educational and learning purposes.