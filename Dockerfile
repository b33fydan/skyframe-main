FROM python:3.10-slim

WORKDIR /app

# Copy the backend directory into the container
COPY skyframe-backend /app/skyframe-backend

# Set working directory to backend
WORKDIR /app/skyframe-backend

# Install dependencies
RUN ls -al /app/skyframe-backend && pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8000

# Run the Gunicorn server, referencing the app inside radius_filter_api.py
CMD ["gunicorn", "--chdir", "skyframe-backend", "radius_filter_api:app", "-w", "2", "-b", "0.0.0.0:8000"]


