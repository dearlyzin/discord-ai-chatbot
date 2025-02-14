from discord import Embed, Color
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        """Displays the list of available commands."""
        embed = Embed(
            title="📚 Command Guide",
            description="Here is what I can do!",
            color=Color.blue()
        )

        embed.add_field(
            name="🤖 Commands",
            value="""
            **!ask [your question]** - Ask the AI a question.
            **!clear** - Clears the AI's memory.
            **!help** - Displays all bot commands.
            """,
            inline=False
        )

        embed.add_field(
            name="💡 Examples:",
            value="""
            **!ask Who are you**
            """,
            inline=False
        )

        embed.add_field(
            name="⚠️ Notes:",
            value="""
            - Wait 5 seconds between questions.
            """,
            inline=False
        )

        embed.set_footer(text="Made with Groq ✅")  # Add your custom footer message here
        await ctx.send(embed=embed)

class Clear(commands.Cog):
    def __init__(self, bot, conversation_memory):
        self.bot = bot
        self.conversation_memory = conversation_memory

    @commands.command(name='clear')
    async def clear(self, ctx):
        """Clears the user's conversation memory."""
        user_id = ctx.author.id

        if user_id in self.conversation_memory:
            del self.conversation_memory[user_id]
            await ctx.send("🧹 Conversation memory has been cleared!")
        else:
            await ctx.send("❌ No memory to clear.")

async def setup(bot):
    """Setup function to add commands to the bot."""
    conversation_memory = {}
    await bot.add_cog(Help(bot))
    await bot.add_cog(Clear(bot, conversation_memory))
