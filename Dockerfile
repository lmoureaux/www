# SPDX-License-Identifier: MIT
#
# Copyright (c) 2019 Michael Herman
# Copyright (c) 2020 Louis Moureaux

from python:3

workdir /home/longturn-www/

# Avoid .pyc files
env PYTHONDONTWRITEBYTECODE 1
# Unbuffered stdin/stdout
env PYTHONUNBUFFERED 1

# Make sure we don't use an outdated version of pip
run pip install --upgrade pip

# Install requirements
copy ./requirements.txt longturn/requirements.txt
run pip install -r longturn/requirements.txt

# Copy the rest
copy . longturn

# Entry point that that flushes the DB and performs migrations
entrypoint ["longturn/docker-entrypoint.sh"]

