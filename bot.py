import json
import logging

import discord
from discord.ext import commands
from duckduckgo_search import ddg

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="-")


def get_token():
    with open('config.json', 'r') as config:
        return json.loads(config.read())["token"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def g(ctx, *args):
    query = ' '.join(args)
    results = ddg(query.strip(), safesearch='Moderate', max_results=3)
    output = ""
    for i, result in enumerate(results, 1):
        output += f"{i}. {result['title']} (<{result['href']}>)\n> {result['body']}\n"
    await ctx.send(output)


@client.command()
async def ping(ctx):
    await ctx.send("hi yes hello im not dead i think")

client.run(get_token())
