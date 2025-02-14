Discord AI Chatbot

🤖 Description
An intelligent chatbot for Discord that utilizes the Groq API for faster responses. The bot allows you to:

✅ Change the AI model according to Groq's available options.
✅ Maintain conversation memory for multiple users simultaneously.
✅ Use it for free with a generous daily usage limit.
✅ Expand functionality by easily adding more commands.

Main Commands
!ask [your question] → Ask the AI a question.
!help → Displays help information.
!clear → Clears conversation memory.


🚀 How to Set Up
1️⃣ Clone the Repository
git clone https://github.com/your-username/discord-ai-chatbot.git
cd discord-ai-chatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file in the root directory and add the following:

DISCORD_TOKEN=your_discord_bot_token
GROQ_API_KEY=your_groq_api_key
Replace your_discord_bot_token and your_groq_api_key with your actual tokens.

4️⃣ Run the Bot
python bot.py

🛠️ Project Structure
discord-ai-chatbot/
│
├── bot.py                # Main bot file
├── cmd_helpers.py        # Helper commands (e.g., !help)
├── ask.py                # Core chatbot functionality
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── utils/
    └── helpers.py        # Utility functions

🌐 How to Use
Invite the Bot: Use the OAuth2 URL to add the bot to your server.
Ask Questions: Use !ask [your question] to interact with the AI.
Clear Memory: Use !clear to reset the conversation memory.