# syntax=docker/dockerfile:1
FROM alpine
RUN apk add python3 py3-pip
RUN python3 -m pip install discord.py duckduckgo_search
WORKDIR /app
COPY ./bot.py .
COPY ./config.json .
CMD ["python3", "bot.py"]
