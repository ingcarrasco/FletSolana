FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r InfraApp/requirements.txt
RUN pwd && ls

EXPOSE 8999

ENTRYPOINT [ "sh", "entrypoint.sh" ]