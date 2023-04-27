import discord
import asyncio
import random

# Replace these with your own values
token = str("YOUR TOKEN HERE")
GUILD_ID = SERVER ID HERE
CHANNEL_ID = CHANNEL ID HERE

client = discord.Client()

@client.event
async def send_message(client):
        guild = client.get_guild(int(GUILD_ID))
        channel = guild.get_channel(CHANNEL_ID)
        message_content = ("YOUR MESSAGE HERE")
        await channel.send(message_content)

@client.event
async def on_ready():
    try:
        print(f"Logged in as {client.user} (ID: {client.user.id})")
        while True:
            await send_message(client)
            wait_time = random.randint() #<-- Waiting time range between posts. This HAS to be in SECONDS. e.g. 2 hours to 2.5 hours: 2*60*60, 2*60*75
            print(f"Waiting for {wait_time} seconds...")
            await asyncio.sleep(wait_time)
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")

print("Token= ", token)
client.run(token, bot=False)
