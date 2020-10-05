FROM python:3.8-slim-buster as base
RUN mkdir /install
WORKDIR /install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir 

FROM base
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]

