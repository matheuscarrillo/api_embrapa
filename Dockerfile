# # syntax=docker/dockerfile:1
# ARG PYVERSION=3.10-slim-buster

# FROM python:${PYVERSION}
# ENV PORT=8080
# EXPOSE 8080
# ENV PYTHONWARNINGS=ignore
# ENV PYDEVD_THREAD_DUMP_ON_WARN_EVALUATION_TIMEOUT=false
# ENV APP_WORKDIR=/app
# RUN apt update && apt upgrade -y \
#     && apt install ca-certificates curl apt-transport-https lsb-release gnupg gcc musl-dev libpq-dev -y \
#     && apt clean autoclean \
#     && apt autoremove -y \
#     && rm -rf /var/lib/{apt,dpkg,cache,log} \
#     && python3 -m pip install --upgrade pip \
#     && pip install google-cloud-storage

# WORKDIR ${APP_WORKDIR}

# # Install poetry
# RUN pip install "poetry==1.2.2"

# # Copy only requirements to cache them in docker layer
# WORKDIR ${APP_WORKDIR}
# COPY . ${APP_WORKDIR}/routes/
# WORKDIR ${APP_WORKDIR}/routes
# RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2"]
# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Comando para rodar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2"]