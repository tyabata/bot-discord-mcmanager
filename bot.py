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
    await channel.send('bot起動! : 使い方は @manager_bot help で聞いてね')

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

        elif text == 'start':
            # サーバ起動
            result = gcp.startServer()
            await reply.sendStartServerMessage(data, result)

        elif text == 'stop':
            # サーバ停止
            result = gcp.stopServer()
            await reply.sendStopServerMessage(data, result)
        
        elif text == 'state':
            result = gcp.getServerState()
            await reply.sendServerInfo(data, result)
    
        elif text == 'request':
            # 機能要望など
            await data.add_reaction("👍")
            await data.pin()
            await reply.sendPinnedAfterMessage(data)
        
        else:
            # 未対応のメンションに対しての返信
            await reply.sendOtherMessage(data)

    # メンションつき以外は基本無視

# 起動
client.run(TOKEN)