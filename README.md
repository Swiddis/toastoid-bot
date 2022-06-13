# Toastoid

A simple utilities bot for a very lazy developer.

## Description

Toastoid is a (currently) simple Discord.py bot with quite limited functionality. It's meant to be a convenience utilities bot, supplying basic web functionality for when you're too lazy to open a browser. It's also a personal experiment in docker containerization.

This project should probably not be seriously used as a Discord bot in a sizeable server, I'm running it exclusively on small servers with my friends.

Currently, the implemented commands are:
- **ping**: Ping the bot, make sure it's not dead.
- **g [query]**: Short for 'google', but actually searches DuckDuckGo. Returns top 3 results for query.
- **kv [set/add] [key] [value?]**: A simple public key-value store using SQLite. Good for leaving silly notes.

## Getting Started

### Dependencies

* [Docker](https://www.docker.com/)

### Installing

You need to [create a discord bot](https://discord.com/developers) and store the token in a `token.txt` file.

The project runs as a composed docker container using a local volume and pulling code from this repository. Strictly speaking you only need the docker files and a `token.txt` file in the same directory. That is, the directory structure should look like:

```
toastoid
- docker-compose.yml
- Dockerfile
- token.txt
```

The easiest way to accomplish this is to clone the repository and add the token file.

### Executing program

When you have the directory set up, simply build and run the containers:

```sh
docker-compose up -d --build
```

You can stop the bot by composing down:

```sh
docker-compose down
```

## License

This project is licensed under the MIT License - see the LICENSE file for details
