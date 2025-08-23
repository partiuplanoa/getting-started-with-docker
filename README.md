# Getting started with docker 

In this resp you will learn about what is docker and how you can create a docker project

### What is Docker?
Docker is a tool that lets you package your entire project, system, and all its dependencies into a single “box” called an image. You can run this box anywhere—no more system errors or missing dependencies.

### Why is Docker useful?
Imagine you have a Flask app. To run it on another computer, you’d have to install Python, Flask, and every other required package, and hope the versions match. With Docker, everything is bundled together, so it just works.

---

### What you will Learn
- Python and How to create Monitoring Application in Python using Flask and psutil
- How to run a Python App locally.
- Learn Docker and How to containerize a Python application:
- Creating Dockerfile
- Building DockerImage
- Running Docker Container
- Docker Commands

### Prerequisites !

- Code editor (Vscode)
- Python3 Installed.
- Docker Installed.

## ✨Let’s Start the Project ✨


### ✅ Step 1: Create a Flask app
Write your Python Flask app (for example, an app that shows CPU/RAM data in the browser). download the zip file and extract it open in vs code and hit the below commands and run this command to install all `requirements` after install all the requirements run the app by writing `app.py`. The app is now running at port `http://127.0.0.1:5000/`. 🚀 

```bash
pip install -r requirements.txt
```

### ✅ Step 2: Create and Write a Dockerfile
Create a Dockerfile in the root directory of the project with the following contents.
- A Dockerfile is a instruction list for Docker.
  
Example:
```python
# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app when the container is run
CMD ["flask", "run"]
```

