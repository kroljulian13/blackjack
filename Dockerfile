FROM alpine:3.5
RUN apk add --update python3 py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY . /src
CMD python /src/app.py