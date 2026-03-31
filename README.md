# Legal Case CI/CD App

This project is a stronger starter version of the legal CI/CD application described in your PDFs. It keeps the same core architecture:

- FastAPI application
- GitHub for source control
- Pytest for automated testing
- Docker for containerization
- GitHub Actions for CI/CD
- Free-friendly deployment option using a self-hosted runner

## Features

- `GET /health` for deployment verification
- `GET /users` to return seeded user data
- `GET /cases` to return seeded legal cases
- `POST /cases` to create a new legal case
- `POST /auth/login` for a simple demo login flow
- Minimal dashboard at `/`

## Project Structure

```text
app/
  main.py
  database.py
  models.py
  routes/
  static/
tests/
.github/workflows/ci.yml
.github/workflows/cd-self-hosted.yml
Dockerfile
requirements.txt
README.md
```

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn app.main:app --reload
```

4. Open:

- `http://localhost:8000`
- `http://localhost:8000/health`
- `http://localhost:8000/docs`

## Run Tests

```bash
pytest
```

## Docker

Build:

```bash
docker build -t legal-app .
```

Run:

```bash
docker run -p 8000:8000 legal-app
```

Or with Compose:

```bash
docker compose up --build
```

## Free-Friendly CI/CD Setup

This repo now uses a safer no-AWS-default setup:

- `ci.yml` runs tests on GitHub Actions
- `cd-self-hosted.yml` deploys on a self-hosted runner machine that you control

This avoids automatic charges from AWS ECR, EC2, public IPs, or extra storage.

## Recommended Zero-Cost Path

1. Keep the repository public if possible.
2. Use GitHub-hosted runners for CI.
3. Use a self-hosted runner on your own laptop, old PC, or local server for CD.
4. Install Docker on that machine.
5. Register the machine as a GitHub self-hosted runner.
6. On every push to `main`, GitHub will trigger deployment on that machine using `docker compose up -d --build`.

## Important Billing Notes

- GitHub Actions is free on standard GitHub-hosted runners for public repositories.
- For private repositories, GitHub Free includes limited monthly minutes and storage.
- Self-hosted GitHub runners do not consume GitHub-hosted runner minutes.
- AWS EC2 and ECR can incur charges if your free credits/free tier are exhausted or if your account is not eligible anymore.

## If You Still Want AWS

Use AWS only if you have confirmed your account is still inside the AWS Free Tier or still has free credits available. Check the current AWS billing dashboard before launching:

- EC2 free tier eligibility depends on when the AWS account was created.
- New AWS accounts created on or after July 15, 2025 use credit-based Free Tier plans.
- Private Amazon ECR free usage is limited.

If you want, AWS deployment can be added later as a separate optional workflow.

## Next Improvements

- Replace the in-memory store with PostgreSQL and SQLAlchemy
- Add JWT auth and role-based access control
- Add Terraform for optional AWS infrastructure provisioning
- Add Nginx and HTTPS in front of the EC2-hosted app
