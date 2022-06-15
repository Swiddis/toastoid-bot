FROM alpine/git AS git
RUN git clone --depth 1 https://github.com/Swiddis/toastoid-bot.git /toastoid-bot

FROM python:3.9-alpine
RUN python3 -m pip install discord.py requests
WORKDIR /app
COPY --from=git toastoid-bot .
CMD python3 bot.py
