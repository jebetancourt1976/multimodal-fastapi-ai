FROM python:3.10-slim

WORKDIR /app

# System deps (minimal)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install base deps first (cached)
COPY requirements.base.txt .
RUN pip install --no-cache-dir -r requirements.base.txt

# Install heavy AI deps separately (cached once)
COPY requirements.ai.txt .
RUN pip install --no-cache-dir -r requirements.ai.txt

# Copy app LAST (avoid cache busting)
COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
