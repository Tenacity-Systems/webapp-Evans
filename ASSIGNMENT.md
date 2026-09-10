# 🚀 DevOps Assignment — Tenacity Systems

> **Build it. Automate it. Deploy it. Verify it.**

---

## 📋 Assignment Overview

Welcome to your next DevOps challenge!

You have been given a **three-tier web application** for a fictional technology company called **Tenacity Systems**.

Your task is to take this application and build a complete **CI/CD pipeline using GitHub Actions**.

The pipeline should automatically:


Test
  ↓
Build
  ↓
Push
  ↓
Deploy
  ↓
Verify

You will use **Docker, Docker Compose, GitHub Actions and Docker Hub**.

> ⚠️ **Kubernetes is NOT required for this assignment.**
>
> Use **Docker and Docker Compose** for the deployment.

---

# 🏗️ Application Architecture

The application consists of three main components:

| Component | Technology                    |
| --------- | ----------------------------- |
| Frontend  | HTML, CSS, JavaScript + Nginx |
| API       | Python + Flask                |
| Database  | MongoDB                       |

The application follows this basic architecture:


                    ┌───────────────┐
                    │    Browser    │
                    └───────┬───────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │     Frontend      │
                  │      Nginx        │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │    Flask API      │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │     MongoDB       │
                  └───────────────────┘


The application has already been provided for you.

### 🎨 Application Customisation

You **may redesign or improve the application** if you wish.

For example, you could improve:

* The frontend design
* Colours
* Content
* Layout
* Additional functionality

However, the main focus of this assignment is **DevOps and CI/CD**, not frontend development.

---

# 🎯 Your Mission

Your goal is to create an automated process that takes code from GitHub and ends with a running application deployed using Docker.

By the end of the assignment, you should be able to demonstrate:

```text
Developer
    │
    │ git push
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Test
    │
    ├── Build Docker Images
    │
    ├── Push to Docker Hub
    │
    ├── Deploy with Docker Compose
    │
    └── Verify Application
    │
    ▼
Running Application
```

---

# 1️⃣ Create a GitHub Repository

Create a GitHub repository for your project.

Push the supplied application code into the repository.

Your repository should contain:

* Frontend application
* API application
* Dockerfiles
* Docker Compose configuration
* GitHub Actions workflow

Your GitHub Actions workflow should be located inside:

```text
.github/workflows/
```

---

# 2️⃣ Run the Application Locally

Before creating your CI/CD pipeline, make sure the application works locally.

Use Docker Compose to start the application.

The application should be accessible on:

```text
http://localhost:8080
```

Confirm that:

* The frontend loads correctly.
* The API is working.
* The application can communicate with MongoDB.
* The contact/enquiry functionality works.

You should understand the application before automating its deployment.

---

# 3️⃣ 🐳 Docker Hub

Create **two Docker Hub repositories** for your application.

Use:

```text
tenacity-frontend
tenacity-api
```

Your images should look similar to:

```text
YOUR_USERNAME/tenacity-frontend
YOUR_USERNAME/tenacity-api
```

For example:

```text
student123/tenacity-frontend
student123/tenacity-api
```

MongoDB does **not** need to be built by you.

Use the MongoDB image provided in the Docker Compose configuration.

---

# 4️⃣ 🔐 GitHub Secrets

Your GitHub Actions pipeline needs to authenticate with Docker Hub.

Create the following GitHub repository secrets:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Use a **Docker Hub access token**.

### ⚠️ Security Requirement

Do **not**:

* Hard-code your Docker Hub password.
* Hard-code your Docker Hub token.
* Commit credentials to Git.
* Expose credentials in workflow logs.

Credentials must be handled securely using **GitHub Secrets**.

---

# 5️⃣ ⚙️ Build the GitHub Actions Pipeline

Create a GitHub Actions workflow that follows this process:

```text
┌─────────┐
│  TEST   │
└────┬────┘
     │
     ▼
┌─────────┐
│  BUILD  │
└────┬────┘
     │
     ▼
┌─────────┐
│  PUSH   │
└────┬────┘
     │
     ▼
┌─────────┐
│ DEPLOY  │
└────┬────┘
     │
     ▼
┌─────────┐
│ VERIFY  │
└─────────┘
```

Your workflow should contain the following stages.

---

## 🧪 Stage 1 — Test

Create a GitHub Actions job that:

* Checks out the repository.
* Sets up Python.
* Installs the API requirements.
* Runs the API tests using `pytest`.

The pipeline must fail if the tests fail.

Testing must happen **before deployment**.

---

# 🐳 Stage 2 — Build

Build the two application Docker images:

```text
tenacity-frontend
tenacity-api
```

Use the Dockerfiles supplied with the project.

You do **not** need to build the MongoDB image.

---

# 📦 Stage 3 — Push

Authenticate to Docker Hub using your GitHub Secrets.

Push both application images to Docker Hub.

Each image must have at least **two tags**:

```text
latest
```

and:

```text
Git commit SHA
```

For example:

```text
yourusername/tenacity-api:latest
```

and:

```text
yourusername/tenacity-api:<commit-sha>
```

Do the same for the frontend image.

---

# 🚀 Stage 4 — Deploy

Deploy the application using:

```text
Docker Compose
```

The deployment should run on a:

* Docker-enabled server
* GitHub Actions self-hosted runner

Your deployment should:

1. Pull the application images from Docker Hub.
2. Start the application using Docker Compose.
3. Keep MongoDB data persistent.
4. Make the frontend available on port:

```text
8080
```

### Important

The application images should **not be manually built on the deployment server**.

The expected flow is:

```text
GitHub Actions
      │
      │ Build
      ▼
Docker Images
      │
      │ Push
      ▼
Docker Hub
      │
      │ Pull
      ▼
Deployment Server
      │
      ▼
Docker Compose
```

---

# ❤️ Stage 5 — Verify

After deployment, your pipeline must verify that the application is working.

Use the API health endpoint:

```text
http://localhost:8080/api/health
```

The workflow should fail if the application is not healthy.

A successful deployment should show that the API and database are available.

---

# 🔀 Pull Requests vs Main Branch

Your workflow should handle pull requests and the `main` branch appropriately.

### Pull Request

When a pull request is created, your workflow should at least:

```text
Run Tests
```

A pull request should **not deploy the application**.

### Main Branch

When changes are pushed or merged into `main`, the pipeline should perform the complete process:

```text
Test
  ↓
Build
  ↓
Push
  ↓
Deploy
  ↓
Verify
```

---

# 📁 Expected Project Structure

Your project should contain the application and CI/CD configuration.

At minimum, you should have:

```text
project/
│
├── api/
│   └── Dockerfile
│
├── frontend/
│   └── Dockerfile
│
├── docker-compose.yml
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# 📤 Required Deliverables

At the end of the assignment, submit the following.

## 1. GitHub Repository

Provide the URL of your GitHub repository.

```text
https://github.com/YOUR_USERNAME/YOUR_REPOSITORY
```

---

## 2. GitHub Actions Workflow

Your workflow must be included in:

```text
.github/workflows/
```

---

## 3. Dockerfiles

Include:

```text
frontend/Dockerfile
api/Dockerfile
```

---

## 4. Docker Compose

Include:

```text
docker-compose.yml
```

---

## 5. Successful GitHub Actions Run

Provide a screenshot showing your GitHub Actions pipeline completing successfully.

The screenshot should clearly show the required stages completing successfully.

---

## 6. Running Application

Provide a screenshot showing the **Tenacity Systems website running through Docker**.

The application should be accessed through the Docker deployment, for example:

```text
http://<server-ip>:8080
```

Do not submit a screenshot of a locally opened HTML file such as:

```text
file:///...
```

---

## 7. Health Check

Provide a screenshot showing the API health endpoint working:

```text
/api/health
```

---

## 8. Docker Hub

Provide evidence that both application images have been successfully pushed to Docker Hub.

You should be able to show:

```text
tenacity-frontend
```

and:

```text
tenacity-api
```

Your completed pipeline should achieve:

```text
                 ┌──────────────┐
                 │    GitHub    │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │     TEST     │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │     BUILD    │
                 │    DOCKER    │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │     PUSH     │
                 │  DOCKER HUB  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │    DEPLOY    │
                 │    COMPOSE   │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │    VERIFY    │
                 │   HEALTH     │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   SUCCESS!   │
                 │ APPLICATION  │
                 │    RUNNING   │
                 └──────────────┘
```

## 🏆 Good luck!

**Build something reliable. Automate everything you can. And remember — if it works once manually, the real DevOps challenge is making it work automatically every time.**

```
```

