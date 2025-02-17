from discord import Embed, Color
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='h')
    async def help(self, ctx):
        embed = Embed(
            title="📚 Command Guide",
            description="Here's what I can do!",
            color=Color.blue()
        )

        embed.add_field(
            name="🤖 Commands",
            value="""
            **!ask [your question]** - Ask something to the AI.
<<<<<<< HEAD

            **!clear** - Clears the AI's memory.

            **!h** - Shows all bot commands.

=======
            **!clear** - Clears the AI's memory.
            **!h** - Shows all bot commands.
>>>>>>> 77e35faa746000d15cc66a5a62d84fa54ac4d364
            """,
            inline=False
        )

        embed.add_field(
            name="💡 Examples:",
            value="""
<<<<<<< HEAD
            **!ask Who are you?** - Ask the AI about itself.
=======
            **!ask Who are you?**
>>>>>>> 77e35faa746000d15cc66a5a62d84fa54ac4d364
            """,
            inline=False
        )

        embed.add_field(
            name="⚠️ Notes:",
            value="""
<<<<<<< HEAD
            - **Wait 5 seconds between questions.**
=======
            - Wait 5 seconds between questions.
>>>>>>> 77e35faa746000d15cc66a5a62d84fa54ac4d364
            """,
            inline=False
        )

        embed.set_footer(text="Made by DEARLY ")
        await ctx.send(embed=embed)

class Clear(commands.Cog):
    def __init__(self, bot, conversation_memory):
        self.bot = bot
        self.conversation_memory = conversation_memory

    @commands.command(name='clear')
    async def clear(self, ctx):
        user_id = ctx.author.id

        if user_id in self.conversation_memory:
            del self.conversation_memory[user_id]
            await ctx.send("🧹 Conversation memory cleared!")
        else:
            await ctx.send("❌ No memory to clear.")

async def setup(bot):
    conversation_memory = {}
    await bot.add_cog(Help(bot))
    await bot.add_cog(Clear(bot, conversation_memory))
