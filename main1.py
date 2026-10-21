import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set")

TARGET_CHANNEL_ID = 1562184351020617728

class AutoResponderBot(discord.Client):
    async def on_ready(self):
        print(f'Бот {self.user} подключился')

    async def on_message(self, message):
        # Защита от само-ответа
        if message.author.id == self.user.id:
            return

        # ЕСЛИ сообщение написано НЕ в целевом канале — бот его полностью игнорирует
        if message.channel.id != TARGET_CHANNEL_ID:
            return

        # Ответ заготовленным сообщением
        await message.channel.send('Осуждаю')

intents = discord.Intents.default()
intents.message_content = True

client = AutoResponderBot(intents=intents)
client.run(TOKEN)