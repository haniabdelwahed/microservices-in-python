FROM python:3.8.13-alpine
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY src src
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
            CMD curl -f http://localhost/appcheck || exit 1
ENTRYPOINT [ "python", "./src/app.py"]