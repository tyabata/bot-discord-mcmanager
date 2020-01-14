import discord

from modules import reply
from modules import gcp

import os

CHANNEL_ID = int(os.environ['DISCORD_CHANNEL_ID'])
TOKEN = str(os.environ['DISCORD_TOKEN'])

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('bot起動! : 使い方は @kodaking_bot help で聞いてね')

#
# やりとり
# 
@client.event
async def on_message(data):

    if data.author.bot:
        # botは対象外(自分込み)
        return
    
    if client.user in data.mentions:
        text = data.content.split()[1]

        if text == 'help':
            # helpを表示する
            await reply.sendHelpMessage(data)
            return

        if text == 'start':
            await gcp.startServer()
            return

        if text == 'stop':
            await gcp.stopServer()
            return

        # 未対応のメンションに対しての返信
        await reply.sendOtherMessage(data)

    # other


# 起動
client.run(TOKEN)