from discord import Embed, Color

## Função para dividir a mensagem em partes menores para evitar erros de limite de tamanho

def dividir_mensagem(mensagem, limite=1024):
    partes = []
    while len(mensagem) > limite:
        corte = mensagem.rfind(' ', 0, limite)
        if corte == -1:
            corte = limite
        partes.append(mensagem[:corte])
        mensagem = mensagem[corte:].strip()
    partes.append(mensagem)
    return partes

def criar_embed_resposta(pergunta, resposta):
    embed = Embed(color=Color.blue())
    embed.add_field(name="📝 Pergunta", value=pergunta, inline=False)
    partes_resposta = dividir_mensagem(resposta, limite=1024)
    for i, parte in enumerate(partes_resposta):
        embed.add_field(name=f"💭 Resposta (Parte {i + 1})", value=parte, inline=False)
    embed.set_footer(text="Feito com Groq✅") ## Coloque sua mensagem aqui  
    return embed
