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

The project runs in a docker container. After installing cloning and navigating to the repo, you can build the container with a specified tag using:

```sh
docker build -t toastoid .
```

This will use the repository's Dockerfile to create a small linux environment (through [Alpine](https://alpinelinux.org/)) and automatically install Python, Discord.py, and additional dependencies.

### Executing program

After setting up the container, simply run the image by tag and give it a name:

```sh
docker run --name toastoid toastoid
```

You can stop it by the name it was started under:

```sh
docker stop toastoid
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
