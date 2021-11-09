FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app.py /app/

WORKDIR /app
