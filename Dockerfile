# syntax=docker/dockerfile:1
ARG PYVERSION=3.10-slim-buster

FROM python:${PYVERSION}
ENV PORT=8080
EXPOSE 8080
ENV PYTHONWARNINGS=ignore
ENV PYDEVD_THREAD_DUMP_ON_WARN_EVALUATION_TIMEOUT=false
ENV APP_WORKDIR=/app
RUN apt update && apt upgrade -y \
    && apt install ca-certificates curl apt-transport-https lsb-release gnupg gcc musl-dev libpq-dev -y \
    && apt clean autoclean \
    && apt autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log} \
    && python3 -m pip install --upgrade pip

WORKDIR ${APP_WORKDIR}

# Install poetry
RUN pip install "poetry==1.2.2"

# Copy only requirements to cache them in docker layer
WORKDIR ${APP_WORKDIR}
COPY . ${APP_WORKDIR}/acerto_ingestion_blip/
WORKDIR ${APP_WORKDIR}/acerto_ingestion_blip
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
