import logging
import os
import queue
import urllib.parse

import discord
from discord.ext import commands
from requests.exceptions import ReadTimeout

import kval
from ddg import ddg

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="-")
kvdb = kval.KValDb()


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
async def kv(ctx, op, key, *args):
    output = 'Invalid Command'
    if op == 'set':
        kvdb.set_item(key, ' '.join(args))
        output = f"Set key {key}"
    elif op == 'get':
        items = kvdb.get_item(key)
        output = items[0] if items else "Key does not exist"
    await ctx.send(output)


@client.command()
async def ping(ctx):
    await ctx.send("hi yes hello im not dead i think")

with open('/run/secrets/token', 'r') as token_file:
    client.run(token_file.read())
