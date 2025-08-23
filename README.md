# Getting started with docker 

This repository will guide you step by step on what Docker is and how to containerize your Python project. By the end, you’ll have a fully working Dockerized Flask app.
![banner](templates/banner.webp)


### What is Docker?
Docker is a tool that lets you package your entire application, including all dependencies, libraries, and system tools, into a single “container” called an image. This container can run anywhere, eliminating the classic “it works on my machine” problem.

Think of Docker as a portable box for your project—you can move it from one computer to another, and it will work exactly the same.

### Why is Docker useful?
Imagine you have a Flask app. To run it on another computer, you’d have to install Python, Flask, and every other required package, and hope the versions match. With Docker, everything is bundled together, so it just works.

---

### 💡What you will Learn
- Python and How to create Monitoring Application in Python using Flask and psutil
- How to run a Python App locally.
- Learn Docker and How to containerize a Python application:
- Creating Dockerfile
- Building DockerImage
- Running Docker Container
- Docker Commands

### 👆🏻Prerequisites !

- Code editor (Vscode)
- Python3 Installed.
- Docker Installed.

### 1️⃣ Folder Structure (Recommended)
```markdown
docker-monitoring-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── index.html
```

## ✨Let’s Start the Project ✨


### ✅ Step 1: Create a Flask app
Write your Python Flask app (for example, an app that shows CPU/RAM data in the browser). download the zip file and extract it open in vs code and hit the below commands and run this command to install all `requirements` after install all the requirements run the app by writing `app.py`. The app is now running at port `http://127.0.0.1:5000/`. 🚀 

```bash
pip install -r requirements.txt
```
Run the Flask app:
```bash
python app.py
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
Explanation:
- **FROM**: Base image for Python environment
- **WORKDIR**: Directory inside the container
- **COPY** + RUN: Install dependencies
- **EXPOSE**: Open port for the app
- **CMD**: Command to start Flask

### ✅ Step 3: Build the Docker image
Run:
```bash
docker build -t my-app .
```
- This turns your code, dependencies, and setup into a portable image.

### ✅ Step 4: Run the container locally
Run:
```bash
docker run -p 5000:5000 my-app
```
Open your browser to localhost:5000—your app is running!
- The app now runs in an isolated container, independent of your system.
- Open your browser at: http://localhost:5000
- You should see your Flask monitoring dashboard running perfectly.

### ✅ Summary
By completing this project, you now know how to:
1. Build a Python Flask app
2. Write a Dockerfile to containerize it
3. Build and run a Docker image
4. Access your app from any machine without worrying about dependencies
Docker makes your projects portable, consistent, and easy to share.

