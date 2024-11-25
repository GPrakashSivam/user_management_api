# Using the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Expose the port the app will run on
EXPOSE 8000

# Command to run the gunicorn server serving our Django API
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "user_management_project.wsgi:application"]
