# Use a base image
FROM python:3.11.6

# Set the working directory
WORKDIR /app

# Copy the backend files to the working directory
COPY . /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Expose the necessary port
EXPOSE 1629

# Define the command to run the backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1629"]
