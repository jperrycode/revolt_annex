FROM python:3.10.7-alpine

# Install build dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev gcc musl-dev && \
    pip install --upgrade pip

# Install psycopg2-binary
RUN pip install psycopg2-binary

WORKDIR /revolt_annex

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]