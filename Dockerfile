# Use an official Python image as the base image
FROM python:3.13.0b1-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the application dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY app.py .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port on which the Flask application will run
EXPOSE 5000

# Define the command to run when the container is started
CMD ["flask", "run", "--host=0.0.0.0"]
