FROM python:3.9-alpine
RUN python3 -m pip install discord.py pymongo requests
WORKDIR /app
COPY . .
CMD python3 bot.py
