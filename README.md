# 🤖 **Discord AI Chatbot**  

## 📌 **Description**  
An intelligent chatbot for Discord that utilizes the **Groq API** for faster responses.  

🔹 **Key Features:**  
✅ Change the AI model according to [Groq's available models](https://console.groq.com/docs/models).  
✅ Maintain conversation memory for multiple users simultaneously.  
✅ Use it for free with a generous daily usage limit.  
✅ Expand functionality by easily adding more commands.  

---

## ⚙️ **Main Commands**  
````yaml
!ask [your question] → Ask the AI a question.
!h → Displays help information.
!clear → Clears conversation memory.
````

---

🚀 **How to Set Up**

🔹 1️⃣ Clone the Repository
````yaml
git clone https://github.com/dearlyzin/discord-ai-chatbot.git
````
🔹 2️⃣ Install Dependencies
````yaml
pip install -r requirements.txt
````
🔹 3️⃣ Configure Environment Variables

Create a .env file in the root directory and add the following:
````yaml
DISCORD_TOKEN=your_discord_bot_token
GROQ_API_KEY=your_groq_api_key
````
Replace `your_discord_bot_token` and `your_groq_api_key` with your actual tokens.

Get you Groq API Key [here](https://console.groq.com/keys)

🔹 4️⃣ Run the Bot
````yaml
python bot.py
````

---

🌐 How to Use

✔️ **Invite the Bot** → Use the OAuth2 URL to add the bot to your server.

✔️ **See commands** → Use `!h` to list all the commands

✔️ **Ask Questions** → Use `!ask` [your question] to interact with the AI.

✔️ **Clear Memory** → Use `!clear` to reset the conversation memory.

---

🛠 **Technologies Used**

🐍 **Python**

🤖 **Discord API**

⚡ **Groq API** 
