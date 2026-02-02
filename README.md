# AI PR Reviewer (Full Stack)

An end-to-end **AI-powered Pull Request Reviewer** that allows users to submit PR details via a frontend UI, runs an automated AI code review on the backend, and stores all review artifacts in **Amazon S3** for auditability and history.

This project demonstrates a **real-world full-stack workflow** integrating **React, FastAPI, AI logic, and AWS S3**.

---

## 🚀 Features

- 🖥️ React frontend for submitting PR details
- ⚙️ FastAPI backend for processing PR reviews
- 🤖 AI-based PR review logic (merge / do not merge recommendation)
- ☁️ Amazon S3 storage for:
  - Code diffs
  - PR metadata
  - AI review results
- 🕒 Timestamped and versioned PR review history
- 🔐 Secure AWS IAM-based access
- 🌐 CORS-enabled frontend–backend communication

---

## 🏗️ Architecture

React Frontend
|
| (POST /review)
v
FastAPI Backend
|
| AI Review Logic
|
v
Amazon S3 (Versioned Storage)

yaml
Copy code

---

## 📂 Project Structure

ai-pr-reviewer/
│
├── main.py # FastAPI application
├── storage/
│ ├── init.py
│ └── s3_client.py # S3 upload helpers
│
├── frontend/
│ ├── src/
│ │ └── App.jsx # React UI
│ ├── package.json
│ └── vite.config.js
│
├── .gitignore
└── README.md

yaml
Copy code

---

## 🧪 How It Works (End-to-End Flow)

1. User enters:
   - PR title
   - PR description
   - Code diff (changes)
2. React frontend sends data to FastAPI backend
3. Backend:
   - Runs AI-based review logic
   - Generates merge recommendation
4. Backend stores artifacts in S3:
   - `diff.txt` → raw code changes
   - `metadata.json` → PR title & description
   - `ai_review.json` → AI decision
5. AI response is returned to frontend and displayed to user

---

## ☁️ Amazon S3 Storage Format

Each PR review is stored in a **timestamped folder**:

ai-pr-reviewer/prs/ai-pr-reviewer/<timestamp>/
├── diff.txt
├── metadata.json
└── ai_review.json

yaml
Copy code

### Why this design?
- Immutable audit trail
- Easy rollback & history
- Cost-effective long-term storage
- Production-grade logging

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- JavaScript
- Fetch API

### Backend
- Python
- FastAPI
- Uvicorn

### Cloud & Storage
- Amazon S3 (versioning enabled)
- AWS IAM
- Boto3 (AWS SDK for Python)

---

## ▶️ Running the Project Locally

### 1️⃣ Start Backend

```bash
python -m uvicorn main:app --port 8001
Open Swagger:

arduino
Copy code
http://127.0.0.1:8001/docs
2️⃣ Start Frontend
bash
Copy code
cd frontend
npm install
npm run dev

## Run with Docker

```bash
docker pull avani16/ai-pr-reviewer:latest
docker run -p 8000:8000 avani16/ai-pr-reviewer:latest


📊 Monitoring & Alerting

This project includes a complete Kubernetes monitoring and alerting setup to ensure application reliability and fast incident detection.

Stack Used

Prometheus – Metrics collection and alert evaluation

Alertmanager – Alert routing, grouping, and notification handling

Grafana – Metrics visualization and dashboards

kube-prometheus-stack (Helm) – Kubernetes-native monitoring stack

MailHog – In-cluster SMTP server for local email alert testing

Architecture Overview
Application (ai-pr-reviewer)
        ↓
Kubernetes Metrics (kube-state-metrics)
        ↓
Prometheus (monitoring namespace)
        ↓
Alertmanager
        ↓
SMTP (MailHog)
        ↓
Email Inbox (MailHog UI)

Implemented Alerts

AiPrReviewerPodRestarting
Triggers when the application container restarts within the same pod, indicating instability.

KubePodCrashLooping
Detects pods stuck in a CrashLoopBackOff state.

KubeDeploymentReplicasMismatch
Alerts when desired and available replicas differ.

Default Kubernetes alerts
Includes Watchdog, TargetDown, and etcd-related alerts for cluster health.

Alert Delivery Validation

Alerts are validated end-to-end using an in-cluster SMTP server (MailHog).

Both FIRING and RESOLVED email notifications are confirmed.

Alert deduplication and repeat intervals are configured for predictable testing.

MailHog UI allows safe, deterministic testing without external email providers.

Key Learnings

Deleting pods does not increment restart metrics; only container restarts do.

Alertmanager deduplicates alerts and sends notifications only on state changes.

kube-prometheus-stack ships with a default null receiver and must be explicitly overridden for email delivery.

Using MailHog enables reliable local testing without SMTP throttling or silent failures.

Local Access (Development)
# Alertmanager UI
kubectl port-forward -n monitoring pod/alertmanager-kube-prometheus-stack-alertmanager-0 19093:9093

# MailHog UI
kubectl port-forward -n monitoring svc/mailhog 18025:8025

# Grafana UI
kubectl port-forward -n monitoring svc/kube-prometheus-stack-grafana 3000:80

Outcome

This setup provides production-style observability with deterministic local testing, enabling confident monitoring, alert validation, and incident response workflows.

