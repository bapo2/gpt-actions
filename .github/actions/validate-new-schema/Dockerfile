# Use python slim image as the base
FROM python:3.11-slim

# Set the working directory and copy source files
WORKDIR /src
COPY . .

# Make the script executable and install dependencies
RUN chmod +x main.py && pip install pyyaml yamllint

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/src

# Run the script
CMD ["python", "/src/main.py"]