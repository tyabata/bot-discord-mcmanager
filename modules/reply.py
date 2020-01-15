
# helpメッセージ
helpMessage = '''
対応している応答一覧です d(^o^)b

```
help    : これ
request : ピン留めするだけですが、いずれ対応します
start   : サーバを起動します。
stop    : サーバを停止します。
```
'''.strip()

# helpを表示する
async def sendHelpMessage(data):


    await data.channel.send(f'{data.author.mention} {helpMessage}')

# 未対応に対しての返信
async def sendOtherMessage(data):
    await data.channel.send(f'{data.author.mention} 対応してないんじゃ')

# 要望に対しての返信
async def sendPinnedAfterMessage(data):
    await data.channel.send(f'{data.author.mention} あなたの要望をピン留めしました。')
