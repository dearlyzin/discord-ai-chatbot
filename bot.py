import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def load_extensions():
    await bot.load_extension('commands.ask')
    await bot.load_extension('utils.cmd_helpers')

@bot.event
async def on_ready():
    print(f'🤖 {bot.user.name} is online!')
    print('------------------------')
    await bot.change_presence(activity=discord.Game(name="!h for commands"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        try:
            await message.add_reaction("✅")
        except Exception as e:
            print(f"Error adding reaction: {e}")
    await bot.process_commands(message)

async def main():
    try:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)
    except KeyboardInterrupt:
        print("\nShutting down the bot...")
        await bot.close()
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        await bot.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot offline.")
