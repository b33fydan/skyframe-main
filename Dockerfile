FROM python:3.10-slim

WORKDIR /app

COPY skyframe-backend /app/skyframe-backend

WORKDIR /app/skyframe-backend

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 8000

# Launch using Gunicorn (better for production than built-in Flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "radius_filter_api:app"]
