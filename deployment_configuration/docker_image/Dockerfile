FROM python:3.7


RUN wget https://github.com/dnatalchuk/python3-http-based-api/archive/master.tar.gz && \
    tar xf ./master.tar.gz && \
    chmod -R 755 python3-http-based-api-master && \
    cd python3-http-based-api-master && \
    pip install -r requirements.txt

WORKDIR python3-http-based-api-master/api

EXPOSE 5000

CMD ["python", "server.py"]