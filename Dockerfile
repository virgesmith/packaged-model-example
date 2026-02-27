# FROM python:3.13.12-trixie

FROM astral/uv:python3.13-trixie

WORKDIR /app

COPY . /app

CMD ["uv", "run", "model"]
