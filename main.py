import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ВЫ ТУТ {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("ПРИВЕТ!")
    elif message.content.startswith('$kakdela'):
        await message.channel.send("Норм")
    elif message.content.startswith('$arduinotop'):
        await message.channel.send("да")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("ТУТ ДОЛЖЕН БЫТЬ TOKEN ТВОЕГО БОТА")
