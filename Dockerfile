# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variable for Python to run unbuffered
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "revolt_annex.wsgi:application", "--bind", "0.0.0.0:8000"]
