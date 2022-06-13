import logging
import os
import queue
import urllib.parse
from requests.exceptions import ReadTimeout

import discord
from discord.ext import commands
from ddg import ddg

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def g(ctx, *args):
    query = ' '.join(args)
    try:
        results = await ddg(query, max_results=3)
        output = ""
        if len(results) == 0:
            await ctx.send("No results (likely due to API error)")
            return
        for i, result in enumerate(results, 1):
            output += f"{i}. {result['title']} (<{result['href']}>)\n> {result['body']}\n"
        await ctx.send(output)
    except ReadTimeout:
        await ctx.send("Timed out while waiting for results")


@client.command()
async def ping(ctx):
    await ctx.send("hi yes hello im not dead i think")

client.run(os.environ["token"])
