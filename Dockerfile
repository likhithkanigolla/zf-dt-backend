# Use a base image
FROM python:3.11.6

# Set the working directory
WORKDIR /app

# Copy the backend files to the working directory
COPY . /app

# Install dependencies
RUN pip install fastapi

# Expose the necessary ports
EXPOSE 8000

# Define the command to run the backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]