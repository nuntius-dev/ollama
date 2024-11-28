# Use the lightweight ubuntu image
FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir fastapi uvicorn requests python-decouple pydantic \
    langchain openai tabulate matplotlib pandas langchain-experimental einops accelerate transformers torch

# Verify the installation of torch (optional but recommended for debugging)
RUN pip show torch

# Set working directory
WORKDIR /app

# Download the app.py file from GitHub
RUN wget -O app.py https://raw.githubusercontent.com/nuntius-dev/ollama/main/app.py

# Expose the port for FastAPI
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
