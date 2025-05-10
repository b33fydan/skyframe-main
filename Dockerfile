FROM python:3.10-slim

WORKDIR /app

# Copy the ENTIRE backend directory
COPY skyframe-backend /app/skyframe-backend

WORKDIR /app/skyframe-backend

RUN ls -al /app/skyframe-backend && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "radius_filter_api:app", "--bind", "0.0.0.0:8000"]
