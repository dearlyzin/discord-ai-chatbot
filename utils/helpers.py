from discord import Embed, Color, utils

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

# Function to create a custom embed
def create_response_embed(question, answer):
    embed = Embed(
        title="🤖 Response",
        description="**Found the answer!**",
        color=Color.blue()
    )
    embed.add_field(name="📝 Question", value=question, inline=False)

    # Split the answer into smaller parts and format each part in bold
    answer_parts = split_message(answer, limit=1024)
    for i, part in enumerate(answer_parts):
        embed.add_field(name=f"💬 Answer (Part {i + 1})", value=f"**{part}**", inline=False)

    # Add timestamp
    embed.timestamp = utils.utcnow()
    return embed
