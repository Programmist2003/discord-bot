import asyncio
import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!remind'):
        args = message.content.split()
        if len(args) < 3:
            await message.channel.send('Usage: !remind <time> <message>')
            return

        time = args[1]
        message = ' '.join(args[2:])

        try:
            delta = timedelta(minutes=int(time))
        except ValueError:
            await message.channel.send('Invalid time format. Please use minutes.')
            return

        reminder_time = datetime.now() + delta

        await message.channel.send(f'Reminder set for {reminder_time.strftime("%H:%M")}')

        await asyncio.sleep(delta.total_seconds())

        await message.channel.send(f'{message.author.mention}, {message}')

client.run('MTIwOTg5ODk4MDc2MzM3MzU5OQ.GSN8Z5.Q8TUSljP7tl9ZDxBwIAz0l2QW-aIJntUDd4Qr4')