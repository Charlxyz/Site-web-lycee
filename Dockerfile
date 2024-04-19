FROM python:3.12

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "Flask", "main.py:app", "--host", "0.0.0.0", "--port", "80" ]