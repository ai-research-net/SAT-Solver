# Use an official Python runtime as a parent image
FROM ubuntu:22.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install system dependencies



RUN apt-get update \
    && apt-get -y install python3 \
    && apt-get clean

# Copy project
COPY . /
WORKDIR /app
COPY src /app/
COPY requirements.txt #/app/requirements.txt

# Install python dependencies
#RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential pkg-config 
RUN python3 -m pip install --upgrade pip


RUN pip install --no-cache-dir -r /requirements.txt
#RUN python3 -m pip install -r /app/requirements.txt

# Run the application:
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5002"]
