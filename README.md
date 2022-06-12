# Toastoid

A simple utilities bot for a very lazy developer.

## Description

Toastoid is a (currently) simple Discord.py bot with quite limited functionality. It's meant to be a convenience utilities bot, supplying basic web functionality for when you're too lazy to open a browser. It's also a personal experiment in docker containerization.

Currently, the implemented commands are:
- **ping**: Ping the bot, make sure it's not dead.
- **g [query]**: Short for 'google', but actually searches DuckDuckGo. Returns top 3 results for query.

## Getting Started

### Dependencies

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)

### Installing

You need to [create a discord bot](https://discord.com/developers) and note the token to use.

The project runs in a docker container pulling code from this repository. Strictly speaking, you only need to copy `Dockerfile` to run it.

After downloading the dockerfile `Dockerfile`, you can build the image with the `toastoid` tag:

```sh
docker build -t toastoid ./path/to/Dockerfile
```

This will create a small linux environment (through [Alpine](https://alpinelinux.org/)) and automatically install Python, Discord.py, and additional dependencies.

### Executing program

After setting up the image, simply run it by tag. You need to supply a token through the environment argument.

```sh
docker run --name toastoid --env token=$DISCORD_BOT_TOKEN toastoid
```

You can stop the bot by the name it was started under:

```sh
docker stop toastoid
```

## License

This project is licensed under the MIT License - see the LICENSE file for details
