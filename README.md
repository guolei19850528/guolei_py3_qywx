# guolei_py3_qywx

## introduce

**guolei python3 qywx library**

## software architecture

~python 3.*

## installation tutorial

```shell
pip install guolei-py3-qywx
```

## catalog description
### Webhook Example
```python
# @see https://developer.work.weixin.qq.com/document/path/91770#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E7%BE%A4%E6%9C%BA%E5%99%A8%E4%BA%BA
from guolei_py3_qywx.webhook import Api as WebhookApi

webhook_api = WebhookApi(
    base_url="https://qyapi.weixin.qq.com/cgi-bin/webhook",
    key="your key"
)
state = webhook_api.send_text(content="测试发送")
if state:
    print("发送成功")
```