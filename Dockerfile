FROM python:3.8-alpine
RUN apk update && apk add bash curl vim
RUN mkdir /app
COPY . /app
RUN pip install --upgrade pip && pip install pipenv 
WORKDIR /app
#RUN pipenv --python 3.8.3
RUN pipenv install --system --deploy --ignore-pipfile
WORKDIR /app/ktrade
EXPOSE 8000/tcp
CMD ["python3.8", "manage.py", "runserver", "0.0.0.0:8000"]