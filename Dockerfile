# Use the official Python image as the base image
FROM python:3.11-slim

# Install netcat
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project files into the container
COPY . .

# Specify the default command to run the Django development server
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
