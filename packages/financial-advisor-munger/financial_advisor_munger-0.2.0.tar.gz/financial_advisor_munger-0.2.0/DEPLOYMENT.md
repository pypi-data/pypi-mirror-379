# Deployment Guide 🚀

Multiple ways to deploy and use the Charlie Munger Investment Analysis API.

## 1. PyPI Package (Recommended)

### Install & Run Locally

```bash
# Install package
pip install financial-advisor-munger[web]

# Start web API
munger-web --port 8000

# Server runs at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### MCP Server for Claude Code

```bash
# Install package
pip install financial-advisor-munger

# Start MCP server
munger-mcp

# Add to Claude Code MCP settings:
{
  "mcpServers": {
    "munger": {
      "command": "munger-mcp",
      "args": []
    }
  }
}
```

## 2. Docker Deployment

### Local Docker

```bash
# Build image
docker build -t munger-api .

# Run container
docker run -p 8000:8000 munger-api

# API available at http://localhost:8000
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  munger-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MUNGER_API_HOST=0.0.0.0
      - MUNGER_API_PORT=8000
    restart: unless-stopped
```

```bash
docker-compose up -d
```

## 3. Railway Deployment

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/...)

### Manual Railway Deployment

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway add
railway deploy

# Your API will be available at https://your-app.railway.app
```

### Environment Variables for Railway

```bash
# In Railway dashboard, add these variables:
MUNGER_API_HOST=0.0.0.0
MUNGER_API_PORT=$PORT  # Railway provides this
```

## 4. Heroku Deployment

### One-Click Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=...)

### Manual Heroku Deployment

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-munger-api

# Set buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku main

# Your API will be available at https://your-munger-api.herokuapp.com
```

### Procfile for Heroku

```
web: munger-web --host 0.0.0.0 --port $PORT
```

## 5. Vercel Deployment (Serverless)

### vercel.json

```json
{
  "builds": [
    {
      "src": "src/financial_advisor_mcp/web_api.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "src/financial_advisor_mcp/web_api.py"
    }
  ]
}
```

```bash
# Deploy to Vercel
npm i -g vercel
vercel --prod
```

## 6. AWS Lambda (Serverless)

### Using Mangum

```python
# lambda_handler.py
from mangum import Mangum
from financial_advisor_mcp.web_api import app

handler = Mangum(app)
```

### SAM Template

```yaml
# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MungerAPI:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Handler: lambda_handler.handler
      Runtime: python3.11
      Events:
        Api:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY
```

## 7. Google Cloud Run

### Dockerfile (optimized for Cloud Run)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -e .[web]

CMD exec munger-web --host 0.0.0.0 --port $PORT
```

### Deploy to Cloud Run

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT-ID/munger-api
gcloud run deploy --image gcr.io/PROJECT-ID/munger-api --platform managed
```

## 8. DigitalOcean App Platform

### .do/app.yaml

```yaml
name: munger-api
services:
- name: api
  source_dir: /
  github:
    repo: your-username/financial-advisor-munger
    branch: main
  run_command: munger-web --host 0.0.0.0 --port $PORT
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  http_port: 8080
```

## 9. Fly.io Deployment

### fly.toml

```toml
app = "munger-api"
primary_region = "dfw"

[build]

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

```bash
# Deploy to Fly.io
fly deploy
```

## Environment Variables

All platforms support these environment variables:

```bash
MUNGER_API_HOST=0.0.0.0      # Host to bind to
MUNGER_API_PORT=8000         # Port to bind to
MUNGER_LOG_LEVEL=info        # Logging level
MUNGER_CACHE_TTL=300         # Cache TTL in seconds
```

## Performance Recommendations

### Production Settings

```bash
# For high-traffic deployments
munger-web --host 0.0.0.0 --port 8000 --workers 4

# With gunicorn (install separately)
gunicorn financial_advisor_mcp.web_api:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Resource Requirements

| Deployment Type | CPU | Memory | Concurrent Users |
|----------------|-----|--------|------------------|
| Development | 0.5 cores | 512MB | 10-50 |
| Production | 1 core | 1GB | 100-500 |
| High-traffic | 2+ cores | 2GB+ | 1000+ |

## Health Checks & Monitoring

### Health Check Endpoint

```bash
# Check if API is healthy
curl http://your-domain/health

# Response:
{
  "status": "healthy",
  "version": "0.2.0",
  "services": {
    "data_provider": "healthy",
    "search": "healthy"
  }
}
```

### Monitoring Endpoints

```bash
# Basic metrics
curl http://your-domain/
curl http://your-domain/docs  # OpenAPI documentation
```

## SSL/HTTPS

Most platforms handle SSL automatically. For custom deployments:

```bash
# Using Let's Encrypt with nginx
certbot --nginx -d your-domain.com
```

## Custom Domain

### Railway
1. Go to Railway dashboard
2. Add custom domain
3. Update DNS records

### Heroku
```bash
heroku domains:add your-domain.com
heroku certs:auto:enable
```

## Usage Examples After Deployment

```python
import requests

# Replace with your deployed URL
API_URL = "https://your-munger-api.railway.app"

# Analyze Apple
response = requests.post(f"{API_URL}/analyze",
                        json={"symbol": "AAPL"})
print(response.json())
```

```javascript
// JavaScript example
const API_URL = "https://your-munger-api.railway.app";

fetch(`${API_URL}/analyze`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({symbol: 'AAPL'})
})
.then(r => r.json())
.then(data => console.log(data));
```

## Troubleshooting

### Common Issues

1. **Port binding errors**: Ensure `MUNGER_API_HOST=0.0.0.0`
2. **Memory issues**: Increase instance memory or add caching
3. **Timeout errors**: Yahoo Finance API occasionally slow
4. **CORS issues**: Configure CORS origins in production

### Debug Mode

```bash
# Enable debug logging
MUNGER_LOG_LEVEL=debug munger-web

# Development mode with auto-reload
munger-web --reload --host 127.0.0.1
```

Choose the deployment method that best fits your needs. Railway and Heroku are great for quick deployments, while Docker gives you maximum control.