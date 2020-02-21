FROM python:3

COPY ./ /app

RUN pip install pipenv && \
    mkdir /data && \
    cd /app && \
    pipenv install --system


WORKDIR /data

ENTRYPOINT [ "/app/run.sh" ]
