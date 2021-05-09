FROM python

USER root

WORKDIR /app
RUN rm -rf /app/*
COPY scripts /app/scripts/
COPY src /app/src
RUN rm -rf /app/*.egg-info
COPY tests /app/tests
COPY pyproject.toml /app
WORKDIR /app
RUN \
    pip install poetry && \
    pip install pycodestyle && \
    pip install isort
COPY src/api/ /app/
COPY src/api/entrypoint.sh /app/
#RUN pip install poetry




#RUN export
#RUN sh scripts/run_unit_tests.sh
