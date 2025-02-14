import os
import requests
from discord import Embed, Color
from discord.ext import commands
from utils.helpers import create_response_embed

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conversation_memory = {}

    @commands.command(name='ask')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ask(self, ctx, *, question):
        """Ask the AI a question"""
        user_id = ctx.author.id

        base_system = (
            ## AI Personality here
            ## Example: "Hello! I'm an AI assistant, I'm here to help you with any questions you have."
        )

        if user_id not in self.conversation_memory:
            self.conversation_memory[user_id] = [
                {"role": "system", "content": base_system}
            ]

        self.conversation_memory[user_id].append({"role": "user", "content": question})

        async with ctx.typing():
            try:
                headers = {'Authorization': f'Bearer {GROQ_API_KEY}', 'Content-Type': 'application/json'}
                payload = {
                    'model': 'llama-3.3-70b-versatile',  # Select the model - https://api.groq.com/openai/v1/models
                    'messages': self.conversation_memory[user_id],
                    'temperature': 0.8,  # Adjust the AI's creativity
                    'max_tokens': 2048
                }
                response = requests.post(GROQ_API_URL, json=payload, headers=headers)
                response.raise_for_status()
                answer = response.json().get('choices', [{}])[0].get('message', {}).get('content', 'Error generating response.')

                self.conversation_memory[user_id].append({"role": "assistant", "content": answer})

                embed = create_response_embed(question, f"**{answer}**")
                await ctx.send(embed=embed)
            except requests.exceptions.RequestException as e:
                await ctx.send(f"❌ Error communicating with the API: {str(e)}")
            except Exception as e:
                await ctx.send(f"❌ An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(Ask(bot))
