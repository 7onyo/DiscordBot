import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3

load_dotenv()
TOKEN = os.getenv('DISCORD_API_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


def setup_database():
    conn = sqlite3.connect('bot_database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_stats (
            user_id INTEGER PRIMARY KEY,
            hello_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@bot.event
async def on_ready():
    setup_database()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    user_id = ctx.author.id

    conn = sqlite3.connect('bot_database.db')
    c = conn.cursor()

    c.execute('SELECT hello_count FROM user_stats WHERE user_id = ?', (user_id,))
    result = c.fetchone()

    if result is None:
        c.execute('INSERT INTO user_stats (user_id, hello_count) VALUES (?, ?)', (user_id, 1))
        count = 1
    else:
        count = result[0] + 1
        c.execute('UPDATE user_stats SET hello_count = ? WHERE user_id = ?', (count, user_id))

    conn.commit()
    conn.close()

    await ctx.send(f'Hello World! You have said hello to me {count} times.')

bot.run(TOKEN)