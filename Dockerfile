FROM python:2.7.13

CMD ["python", "ez_setup.py"]

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
EXPOSE 80

CMD ["python", "app.py"]