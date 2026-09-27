
FROM python:3.12-slim

# Create a non-root user for security
RUN useradd --create-home appuser

WORKDIR /app

# Copy the Python application into the image
COPY app.py .

# Run the application as a non-root user
USER appuser

EXPOSE 8080

CMD ["python", "-u", "app.py"]