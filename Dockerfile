FROM python:3.13.2-alpine

WORKDIR /album

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5002", "--timeout", "1800", "app:app"]
