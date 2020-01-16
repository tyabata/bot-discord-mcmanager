# SDKを利用したGCPのクライアント

import os
import dataclasses
from googleapiclient import discovery

PROJECT = os.environ['PROJECT_ID']
ZONE = os.environ['INSTANCE_ZONE']
INSTANCE = os.environ['INSTANCE_NAME']

compute = discovery.build('compute', 'v1')

# サーバ情報のデータクラス
@dataclasses.dataclass(frozen = True)
class ServerInfo:
    # サーバ名
    name: str
    # 稼働状態
    state: str
    # マイクラアクセス用 外部ip
    ip: str



# server起動
# https://cloud.google.com/compute/docs/reference/rest/v1/instances/start
def startServer():
    result = compute.instances().start(
        project = PROJECT,
        zone = ZONE,
        instance = INSTANCE
    ).execute()

    return result['status']

# server終了
# https://cloud.google.com/compute/docs/reference/rest/v1/instances/stop
def stopServer():
    result = compute.instances().stop(
        project = PROJECT,
        zone = ZONE,
        instance = INSTANCE
    ).execute()

    return result['status']

# serverの状態を取得する
# https://cloud.google.com/compute/docs/reference/rest/v1/instances/get
def getServerState() -> ServerInfo:
    result = compute.instances().get(
        project = PROJECT,
        zone = ZONE,
        instance = INSTANCE
    ).execute()

    network = result['networkInterfaces'][0]
    accessConfig = network['accessConfigs'][0]

    return ServerInfo(
        name = result['name'],
        state = result['status'],
        ip = accessConfig['natIP']
    )

