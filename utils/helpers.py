from discord import Embed, Color

# Function to split the message into smaller parts to avoid size limit errors
def split_message(message, limit=1024):
    parts = []
    while len(message) > limit:
        cut = message.rfind(' ', 0, limit)
        if cut == -1:
            cut = limit
        parts.append(message[:cut])
        message = message[cut:].strip()
    parts.append(message)
    return parts

def create_response_embed(question, answer):
    embed = Embed(color=Color.blue())
    embed.add_field(name="📝 Question", value=question, inline=False)
    answer_parts = split_message(answer, limit=1024)
    for i, part in enumerate(answer_parts):
        embed.add_field(name=f"💭 Answer (Part {i + 1})", value=part, inline=False)
    embed.set_footer(text="Made with Groq ✅")  # Add your custom footer message here
    return embed
