import os
import requests
from discord import Embed, Color
from discord.ext import commands
from utils.helpers import criar_embed_resposta

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.memoria_conversas = {}

    @commands.command(name='ask')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ask(self, ctx, *, pergunta):
        """Faz uma pergunta para a IA"""
        user_id = ctx.author.id

        sistema_base = (
            ## PERSONALIDADE DA IA AQUI
        )

        if user_id not in self.memoria_conversas:
            self.memoria_conversas[user_id] = [
                {"role": "system", "content": sistema_base}
            ]

        self.memoria_conversas[user_id].append({"role": "user", "content": pergunta})

        async with ctx.typing():
            try:
                headers = {'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json'}
                payload = {
                    'model': 'llama-3.3-70b-versatile', ## AJUSTE O MODELO DA IA AQUI - https://api.groq.com/openai/v1/models
                    'messages': self.memoria_conversas[user_id],
                    'temperature': 0.8, ## AJUSTE A CRIATIVIDADE DA IA AQUI
                    'max_tokens': 2048
                }
                response = requests.post(GROQ_API_URL, json=payload, headers=headers)
                response.raise_for_status()
                resposta = response.json().get('choices', [{}])[0].get('message', {}).get('content', 'Erro ao gerar resposta.')

                self.memoria_conversas[user_id].append({"role": "assistant", "content": resposta})

                embed = criar_embed_resposta(pergunta, f"**{resposta}**")
                await ctx.send(embed=embed)
            except requests.exceptions.RequestException as e:
                await ctx.send(f"❌ Erro ao se comunicar com a API: {str(e)}")
            except Exception as e:
                await ctx.send(f"❌ Ocorreu um erro: {str(e)}")

async def setup(bot):
    await bot.add_cog(Ask(bot))