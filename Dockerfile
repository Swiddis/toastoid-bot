# syntax=docker/dockerfile:1
FROM alpine
WORKDIR /app
RUN apk add python3 py3-pip git
RUN git clone https://github.com/Swiddis/toastoid-bot.git
RUN python3 -m pip install discord.py duckduckgo_search
COPY ./config.json ./config.json
CMD ["python3", "toastoid-bot/bot.py"]
