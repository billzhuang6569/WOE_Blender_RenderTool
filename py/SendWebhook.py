import requests
import json
from datetime import datetime

print(f'所有项目渲染已完成，正在发送 webhook')
print(f'此环节将会触发飞书机器人，向WOE团队发送消息')

with open('finish.json', 'r') as f:
    finish = json.load(f)

# 设置 webhook 的 URL
with open("conf.json", "r") as f:
    conf = json.load(f)
webhook_url = conf["webhook_url"]
if not webhook_url:
    raise ValueError("Webhook URL is empty. Please set a webhook URL in conf.json.")

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 创建 JSON 消息
message = {
    "message": f"所有项目渲染已完成，详情：\n",
    "details": finish + '\n',
    "time": f'{now}'
}

# 发送 webhook
response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
if response.status_code == 200:
    print(f'已发送 webhook')
else:
    print(f'发送 webhook 失败，状态码：{response.status_code}, 响应内容：{response.text}')