FROM python:3.9




ENV http_proxy http://internet.ford.com:83/



ENV https_proxy http://internet.ford.com:83/



WORKDIR /project



ADD . /project


RUN pip install -r requirements.txt



CMD ["python","app.py"]