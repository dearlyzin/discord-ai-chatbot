from discord import Embed, Color
from datetime import datetime, timezone
import re

def split_message(message, limit=1000):
    """Divide mensagens longas em partes menores"""
    parts = []
    while len(message) > limit:
        cut = message.rfind(' ', 0, limit)
        if cut == -1:
            cut = limit
        parts.append(message[:cut])
        message = message[cut:].strip()
    parts.append(message)
    return parts

def clean_citations(text):
    """Remove citações do texto"""
    return re.sub(r'\[\d+\]', '', text).strip()

def create_response_embed(query, answer):
    """Cria uma embed para respostas (função principal usada pelo comando !ask)"""
    embed = Embed(
        title="🔎 Resultado",
        description="**Achei algo para você:**",
        color=Color.blue()
    )

    # Formata a pergunta
    query_parts = split_message(query)
    for i, part in enumerate(query_parts, 1):
        field_name = f"📝 Pergunta (Parte {i})" if len(query_parts) > 1 else "📝 Pergunta"
        embed.add_field(name=field_name, value=part, inline=False)

    # Limpa e formata a resposta
    clean_answer = clean_citations(answer)
    answer_parts = split_message(clean_answer)

    for i, part in enumerate(answer_parts, 1):
        field_name = f"📚 Resposta (Parte {i})" if len(answer_parts) > 1 else "📚 Resposta"
        embed.add_field(name=field_name, value=part, inline=False)

    embed.timestamp = datetime.now(timezone.utc)

    return embed

# Alias para manter compatibilidade
create_ask_embed = create_response_embed
