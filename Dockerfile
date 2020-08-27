FROM python:3.8.2

WORKDIR /src

ADD . /src

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uWSGI

CMD ["uwsgi", "app.ini"]