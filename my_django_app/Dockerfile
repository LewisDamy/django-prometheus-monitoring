# Use the official Python image as the base image
FROM --platform=linux/amd64 python:3.10-alpine

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE my_django_app.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file from one level up into the container
COPY requirements.txt /app/

RUN apk add build-base linux-headers
RUN python -m pip install psutil

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install project dependencies
RUN apk --no-cache add build-base && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

# Copy the entire Django project into the container
COPY . /app/

# Expose the port on which the application will run
EXPOSE 8080

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
