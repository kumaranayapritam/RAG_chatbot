FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
#COPY requirements.txt .
# COPY requirements.txt requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt
# Copy the rest of the application
COPY . .

# Create data directory for temporary file storage
RUN mkdir -p /app/data/temp

# Expose the API port
EXPOSE 8000

# Set environment variables for Pinecone
ENV PINECONE_API_KEY=${PINECONE_API_KEY}
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}

# Command to run the application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]