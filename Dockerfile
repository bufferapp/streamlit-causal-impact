FROM python:3.10

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app.py /app/

WORKDIR /app

CMD ["streamlit", "run", "app.py", "--browser.serverAddress='0.0.0.0'"]
