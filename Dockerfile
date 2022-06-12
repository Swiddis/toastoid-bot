# syntax=docker/dockerfile:1
FROM alpine
WORKDIR /app
RUN apk add python3 py3-pip git
RUN python3 -m pip install discord.py duckduckgo_search
RUN git clone https://github.com/Swiddis/toastoid-bot.git
ENV token=
CMD ["python3", "toastoid-bot/bot.py"]
