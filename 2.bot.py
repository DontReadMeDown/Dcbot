import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('sa'):
        await message.channel.send(f' as hoş geldin {client.user}')
    
    if message.content.startswith('merhaba'):
        await message.channel.send(f' merhaba {client.user}!İsmin güzelmiş')
    if message.content.startswith('bot'):
        await message.channel.send(f' efendim{client.user}?')
    
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
client.run("")