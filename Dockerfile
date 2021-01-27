FROM python:3.9.1-alpine3.12

RUN pip install flask
ENV FLASK_APP=count.py

COPY . /code/
WORKDIR /code/

CMD ["flask", "run", "--host=0.0.0.0", "--port=8082"]
