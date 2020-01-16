from .gcp import ServerInfo

# helpメッセージ
helpMessage = '''
対応している応答一覧です d(^o^)b

```
help    : これ
request : ピン留めするだけですが、いずれ対応します
start   : サーバを起動します
stop    : サーバを停止します
state   : サーバの情報を表示します
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
    await data.channel.send(f'{data.author.mention} 要望をピン留めしました！')

# サーバ起動
async def sendStartServerMessage(data, result):
    if result == 'RUNNING':
        await data.channel.send('@everyone サーバーを起動します')
    elif result == 'DONE':
        await data.channel.send('すでに起動しています')
    else:
        await data.channel.send('なにか問題が起きているかも？')

# サーバ停止
async def sendStopServerMessage(data, result):
    if result == 'RUNNING':
        await data.channel.send('サーバーを停止しました')
    elif result == 'DONE':
        # NOTE : ここに入ることあるかわからない
        await data.channel.send('サーバ停止済み')
    elif result == 'PENDING':
        await data.channel.send('サーバ停止中です')

# サーバ情報を表示
async def sendServerInfo(data, info: ServerInfo):

    state = '起動中' if info.state == 'RUNNING' else '停止'

    message = f'''
    server  : {info.name} state   : {state}
    ip      : {info.ip}
    '''.strip()
    
    await data.channel.send(message)
