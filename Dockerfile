FROM python:3-alpine
WORKDIR /app/
COPY *.py requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/github-scanner.py"]
