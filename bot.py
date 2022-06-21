import logging
import os
import queue
import urllib.parse

import discord
from discord.ext import commands
from requests.exceptions import ReadTimeout

import listdb
from ddg import ddg

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="-")
lsdb = listdb.ListDb()


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
    if op == 'add':
        lsdb.add_entry(ctx.author.id, key, ' '.join(args))
        output = f"Added to list `{key}`."
    elif op == 'get':
        items = lsdb.get_entries(ctx.author.id, key)
        if len(items) > 0:
            output = f"List `{key}`:\n"
            for i, item in enumerate(items, 1):
                output += f"{i}. {item}\n"
            output = output.strip()
        else:
            output = f"List `{key}` does not exist."
    await ctx.send(output)


@client.command()
async def ping(ctx):
    await ctx.send("hi yes hello im not dead i think")


@client.command()
async def echo(ctx, *args):
    await ctx.send(f"{' '.join(args)}")

with open('/run/secrets/token', 'r') as token_file:
    token = token_file.read()
client.run(token)
