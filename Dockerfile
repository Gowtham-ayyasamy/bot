# Use official Python 3.10 image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["bash", "start.sh"]
