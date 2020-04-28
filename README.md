# Virtual Masjid

### Installing software

- [Python 3.7](https://www.python.org/downloads/)
   - Windows 10 users can also install Python from the [Windows Store](https://docs.python.org/3.7/using/windows.html#windows-store)
- [Docker](https://docs.docker.com/docker-for-mac/install/) (Download for your platform)
  - NOTE: if you intend to develop on Windows, you need to have Windows 10 Pro
    or Enterprise to be able to use Docker, and you have to have at least a
    somewhat recent CPU that supports Hyper-V. Any non-Atom CPU from the past 5
    years should more than suffice. Also, it'll break VirtualBox 5.x and older.

### Setting Up a Dev Environment

- After you get Python installed, you need to open a command line (see the
  Django Girls tutorial above) and run `pip3 install pipenv` to be able to
  install packages.
- Once you have pipenv installed, install packages:

```bash
pipenv install
```

## Local Development

Start the dev server for local use:

```bash
docker-compose up
```

That will automatically pull the required images, install packages, and launch the
processes. If you need to rebuild your images (such as when dependencies change),
you can add `--build` to the end of that command to re-fetch images and build.

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

To get to a plain shell, run `docker-compose run --rm web bash`. From there, you
can run Django commands like `pipenv run ./manage.py shell`.

## Running without Docker

Say you don't want to use Docker. Don't worry, here's what you need to get started:

```bash
pipenv install --dev
export DJANGO_SECRET_KEY=your_secret_key
pipenv run python manage.py runserver
```

You'll need to set this up anyway if you're making migrations (i.e. modifying models)
outside the docker shell.


