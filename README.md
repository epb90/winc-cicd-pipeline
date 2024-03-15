# Continuous Deployment

## Introduction

The Winc Continuous Deployment assignment presented various challenges and learning opportunities. Although the assignment initially seemed straightforward, it evolved into a complex endeavor requiring critical thinking and problem-solving skills.

## Components

Throughout the module, I encountered several new concepts and technologies, such as Nginx, Gunicorn, and GitHub Actions. Understanding the relationship between these components took some time and research. Mentors and online resources were instrumental in clarifying concepts and guiding me through the process.

At the core of the deployment process lies the Flask application, hosted on a GitHub repository. Upon pushing changes to the repository, a GitHub Actions workflow is triggered. This workflow includes a pytest to ensure the integrity of the application. If the tests pass, the workflow utilizes SSH to deploy the Flask app to a remote server.

The remote server, in this case, can be either physical or virtual, with Ubuntu as the operating system. On this server, the following components are installed:

- **Flask App:** The web application itself, built using the Flask framework.
- **Gunicorn:** A WSGI HTTP server that bridges the communication between the Flask app and the web server.
- **Nginx:** A web server that serves as a reverse proxy and handles client requests.

## Challenges

The deployment process was not without its challenges. Initially, configuring SSH access and GitHub Secrets posed difficulties. Following GitHub's recommendations for generating SSH keys on the server proved to be insufficient. However, after consulting online tutorials and resources, I successfully set up SSH access and GitHub Secrets, enabling smooth communication between the repository and the remote server.

An alternative deployment method was explored to streamline the process and minimize unnecessary files on the server. This involved utilizing a GitHub Actions workflow to selectively copy essential files from the repository to the server. However, this approach introduced unexpected issues, such as outdated process references and cached versions of the web application.

## Conclusion

While the deployment process presented challenges, it provided valuable insights into CI/CD practices and server management. By leveraging GitHub Actions and essential server technologies, I successfully deployed and maintained a Flask application, enhancing my skills in software development and deployment automation.
