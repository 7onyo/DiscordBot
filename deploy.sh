#!/bin/bash

cd /home/discordbot/DiscordBot || exit

git pull origin main

/home/onion/DiscordBot/venv/bin/pip install -r requirements.txt

sudo systemctl restart discordbot
