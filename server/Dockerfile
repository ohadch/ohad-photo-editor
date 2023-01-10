FROM python:3.9

# Install dependencies
RUN pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Prepare the environment
RUN apt-get update -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Entrypoint
ENTRYPOINT ["waitress-serve", "--port=8000", "--call", "app:create_app"]
