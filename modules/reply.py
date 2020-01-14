# helpを表示する
async def sendHelpMessage(data):
    await data.channel.send(f'{data.author.mention} やあ')

# 未対応に対しての返信
async def sendOtherMessage(data):
    await data.channel.send(f'{data.author.mention} 対応してないんじゃ')


