FROM python

USER root

WORKDIR /app

COPY pyproject.toml /app
COPY src/api/ /app/
COPY src/api/entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

RUN \
    pip install poetry && \
    pip install pycodestyle && \
    pip install isort && \
    pip install flask && \
    pip install python-json-logger && \
    poetry install


WORKDIR /app

WORKDIR /app
#RUN ls -lah /app/entrypoint.sh
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]
