FROM python:3.10-slim

WORKDIR /app

# Copy the entire backend folder
COPY ./skyframe-backend ./skyframe-backend

WORKDIR /app/skyframe-backend

RUN echo "🧾 Listing contents of /app/skyframe-backend before pip install:" && ls -al /app/skyframe-backend

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "radius_filter_api:app", "--bind", "0.0.0.0:8000"]

