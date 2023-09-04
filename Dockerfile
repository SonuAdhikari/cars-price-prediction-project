# pull official base image
# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /app

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# install dependencies
#RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install requests

# copy project
COPY . .

#Expose port
EXPOSE 5000

CMD flask --app app run --host 0.0.0.0