FROM python:2.7.13

COPY . /app
WORKDIR /app

CMD ["python", "ez_setup.py"]
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]