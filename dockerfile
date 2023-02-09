FROM python:3.8

COPY ../ /app/
WORKDIR /app
RUN pip install -r resources/r.txt

CMD ["python","main.py"]