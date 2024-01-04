# Get the base image
FROM python:3.11-slim as base
ADD . /src
WORKDIR /src

# Install git
RUN apt-get update && apt-get install -y git

# Make the script executable
RUN chmod +x /src/update-schemas.py

# Install dependencies
RUN pip install GitPython
RUN pip install requests
RUN pip install PyGithub

# Create a new stage for setting up the environment
FROM base as final
WORKDIR /src
ENV PYTHONPATH=/src

# Add the GitHub token as an environment variable
ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=$GITHUB_TOKEN

# Run the script
CMD [ "python", "/src/update-schemas.py" ]