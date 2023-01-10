FROM python:3.7

# Install dependencies
RUN pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Entrypoint
ENTRYPOINT ["waitress-serve", "--port=8000", "--call", "app:create_app"]
