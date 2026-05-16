#!/bin/bash

cd /home/botuser/DiscordBot || exit

git pull origin main

/home/botuser/DiscordBot/venv/bin/pip install -r requirements.txt

sudo systemctl restart discordbot
