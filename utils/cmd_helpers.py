from discord import Embed, Color
from discord.ext import commands

class Ajuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ajuda')
    async def ajuda(self, ctx):
        """Mostra a lista de comandos disponíveis."""
        embed = Embed(
            title="📚 Guia de Comandos",
            description="Aqui está o que posso fazer!",
            color=Color.blue()
        )

        embed.add_field(
            name="🤖 Comandos",
            value="""
            **!ask [sua pergunta]** - Faça uma pergunta para a IA.
            **!limpar** - Limpa a memória da IA.
            **!ajuda** - Exibe todos os comandos do bot.
            """,
            inline=False
        )

        embed.add_field(
            name="💡 Exemplos:",
            value="""
            **!ask Quem é você**
            """,
            inline=False
        )

        embed.add_field(
            name="⚠️ Observações:",
            value="""
            - Aguarde 5 segundos entre perguntas.
            """,
            inline=False
        )

        embed.set_footer(text="Feito com Groq✅") ## Coloque sua mensagem aqui
        await ctx.send(embed=embed)

class Limpar(commands.Cog):
    def __init__(self, bot, memoria_conversas):
        self.bot = bot
        self.memoria_conversas = memoria_conversas

    @commands.command(name='clear')
    async def limpar(self, ctx):
        """Limpa a memória da conversa do usuário."""
        user_id = ctx.author.id

        if user_id in self.memoria_conversas:
            del self.memoria_conversas[user_id]
            await ctx.send("🧹 Memória da conversa foi limpa!")
        else:
            await ctx.send("❌ Não há memória para limpar.")

async def setup(bot):
    """Função de setup para adicionar os comandos ao bot."""
    memoria_conversas = {} 
    await bot.add_cog(Ajuda(bot))
    await bot.add_cog(Limpar(bot, memoria_conversas))
