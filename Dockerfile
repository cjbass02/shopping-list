# Use a base image with Python
FROM python:3.6-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]

#CMD gunicorn -b 0.0.0.0:5000 app:app --timeout 600
