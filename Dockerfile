FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y python3-tk libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean

ENV DISPLAY=host.docker.internal:0.0

WORKDIR /app

# Copy only requirements first to speed up rebuilds
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now copy the actual app code (after deps are installed)
COPY . .

CMD ["python", "image_classifier_app.py"]
