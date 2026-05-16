# 🚀 Deployment Guide

Complete guide for deploying the Customer Retention Intelligence System.

## Table of Contents

1. [Local Development](#local-development)
2. [Streamlit Cloud](#streamlit-cloud)
3. [Docker](#docker)
4. [Server Deployment](#server-deployment)
5. [Production Checklist](#production-checklist)

---

## Local Development

### Quick Start (Windows)

```bash
# Double-click run_app.bat
# Or from command prompt:
run_app.bat
```

Application opens at `http://localhost:8501`

### Quick Start (Mac/Linux)

```bash
# Make script executable
chmod +x run_app.sh

# Run the script
./run_app.sh
```

### Manual Setup

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

---

## Streamlit Cloud

### Free Deployment (Recommended)

#### Step 1: Prepare Repository

```bash
# Initialize git (if not done)
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: Customer Retention Intelligence System"

# Create GitHub repository
# Push to GitHub
git remote add origin <your-repo-url>
git push -u origin main
```

#### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Select branch: `main`
5. Set main file path: `streamlit_app/app.py`
6. Click "Deploy"

#### Step 3: Configure Secrets

In Streamlit Cloud dashboard:
1. Go to App settings
2. Secrets management
3. Add any required API keys or configurations

```toml
# .streamlit/secrets.toml
MODEL_PATH = "models/"
DATA_PATH = "data/"
```

#### Step 4: Monitor

- Check app status in dashboard
- View logs in "Manage app" section
- Set email alerts for errors

### Benefits
- ✅ Free tier available
- ✅ Automatic redeploy on GitHub push
- ✅ HTTPS included
- ✅ No infrastructure management
- ✅ Easy to scale

---

## Docker

### Build Docker Image

```bash
# Build image
docker build -t churn-prediction:latest .

# Tag for registry (optional)
docker tag churn-prediction:latest <username>/churn-prediction:latest
```

### Run Locally

```bash
# Run container
docker run -p 8501:8501 churn-prediction:latest

# With volume mount for data
docker run -p 8501:8501 -v $(pwd)/data:/app/data churn-prediction:latest

# Background mode
docker run -d -p 8501:8501 --name churn-app churn-prediction:latest

# Check logs
docker logs churn-app

# Stop container
docker stop churn-app
```

### Push to Docker Registry

```bash
# Login to Docker Hub
docker login

# Tag image
docker tag churn-prediction:latest <username>/churn-prediction:latest

# Push
docker push <username>/churn-prediction:latest
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  churn-prediction:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./models:/app/models
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    restart: always
```

Run with:
```bash
docker-compose up -d
```

---

## Server Deployment

### AWS EC2 Deployment

#### 1. Launch EC2 Instance

```bash
# Select Ubuntu 22.04 LTS
# t3.medium or larger
# 2GB+ RAM
# 20GB+ storage
```

#### 2. Install Dependencies

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install Python and pip
sudo apt-get install python3 python3-pip python3-venv -y

# Install git
sudo apt-get install git -y

# Install other dependencies
sudo apt-get install build-essential -y
```

#### 3. Clone and Setup

```bash
# Clone repository
git clone <your-repo-url>
cd streamlit_app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

#### 4. Configure Systemd Service

Create `/etc/systemd/system/churn-prediction.service`:

```ini
[Unit]
Description=Customer Retention Intelligence System
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/streamlit_app
Environment="PATH=/home/ubuntu/streamlit_app/venv/bin"
ExecStart=/home/ubuntu/streamlit_app/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable churn-prediction
sudo systemctl start churn-prediction

# Check status
sudo systemctl status churn-prediction
```

#### 5. Configure Nginx Reverse Proxy

Install Nginx:
```bash
sudo apt-get install nginx -y
```

Create `/etc/nginx/sites-available/churn-prediction`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/churn-prediction /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 6. Enable HTTPS (Let's Encrypt)

```bash
sudo apt-get install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

#### 7. Configure Firewall

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### Google Cloud Run Deployment

```bash
# Authenticate
gcloud auth login

# Create .gcloudignore
echo "venv/" >> .gcloudignore

# Deploy
gcloud run deploy churn-prediction \
  --source . \
  --platform managed \
  --region us-central1 \
  --port 8501 \
  --memory 2Gi \
  --allow-unauthenticated

# View logs
gcloud run logs read churn-prediction --limit 100 --platform managed
```

### Heroku Deployment

```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create churn-prediction-app
heroku config:set STREAMLIT_SERVER_HEADLESS=true
git push heroku main
```

---

## Production Checklist

### Pre-Deployment

- [ ] Code reviewed and tested
- [ ] All dependencies in requirements.txt
- [ ] Models saved and accessible
- [ ] Environment variables configured
- [ ] Secrets stored securely
- [ ] Logging configured
- [ ] Error handling implemented
- [ ] Documentation updated

### Deployment

- [ ] Database backups configured (if applicable)
- [ ] Monitoring alerts set up
- [ ] Auto-scaling policies defined
- [ ] CDN configured (if needed)
- [ ] DNS configured
- [ ] SSL certificate installed
- [ ] Firewall rules applied
- [ ] Load balancer configured

### Post-Deployment

- [ ] Smoke tests passing
- [ ] Performance metrics acceptable
- [ ] Error rates low
- [ ] User feedback collected
- [ ] Hotline staffed (if needed)
- [ ] Rollback plan ready
- [ ] Monitoring active
- [ ] Logs being collected

### Performance Optimization

```bash
# Enable caching
streamlit run app.py --logger.level=warning

# Reduce memory usage
streamlit run app.py --client.maxMessageSize=1

# Optimize for slow connections
streamlit run app.py --client.toolbarMode=minimal
```

### Monitoring & Logging

```bash
# View application logs
journalctl -u churn-prediction -f

# Monitor system resources
htop

# Check disk space
df -h

# Monitor network
netstat -i
```

### Backup & Recovery

```bash
# Backup models
tar -czf models_backup.tar.gz models/

# Backup data
tar -czf data_backup.tar.gz data/

# Restore from backup
tar -xzf models_backup.tar.gz
```

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8501
lsof -i :8501

# Kill process
kill -9 <PID>

# Or use different port
streamlit run app.py --server.port 8502
```

### Memory Issues

```bash
# Increase memory limit (Docker)
docker run -m 4g churn-prediction:latest

# Check memory usage
free -h

# Clear cache
rm -rf ~/.streamlit/cache
```

### Model Loading Issues

```bash
# Verify model files exist
ls -la models/

# Check file permissions
chmod 644 models/*.pkl
chmod 644 models/*.keras

# Check model integrity
python3 -c "import joblib; joblib.load('models/best_lgbm_model.pkl')"
```

### SSL Certificate Issues

```bash
# Renew Let's Encrypt certificate
sudo certbot renew

# Force renewal
sudo certbot renew --force-renewal

# Check certificate expiration
openssl s_client -connect your-domain.com:443 -showcerts
```

---

## Performance Benchmarks

Expected performance metrics:

| Metric | Value |
|--------|-------|
| Page Load Time | < 2s |
| Prediction Time | < 1s |
| Model Training | ~5 minutes |
| Memory Usage | 500MB - 2GB |
| Concurrent Users | 100+ |

---

## Support & Maintenance

- 📧 Report issues: [email]
- 🐙 GitHub issues: [link]
- 📚 Documentation: [link]
- 💬 Chat support: [link]

---

**Last Updated**: January 2024
**Version**: 1.0.0
