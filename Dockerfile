FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies
COPY req.txt /code/
RUN pip install -r req.txt


# Copy project
COPY . /code/


RUN python manage.py collectstatic --noinput

CMD python manage.py migrate && gunicorn app.wsgi:application --bind 0.0.0.0:8000
