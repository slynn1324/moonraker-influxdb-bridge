FROM docker.io/python:3.11-alpine

COPY ./mib.py /mib.py

ENTRYPOINT ["python3", "-u", "/mib.py"]

