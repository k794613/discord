import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"已登入：{client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content

    if content and all(c == "3" for c in content):
        await message.channel.send(content + "3")

# 👉 從 Render 讀 token
token = os.getenv("DISCORD_TOKEN")

if not token:
    raise Exception("DISCORD_TOKEN 沒設定")

client.run(token)