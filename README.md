## 介绍

**企业微信 API**

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-qywx
```

## 目录说明

### Webhook Api 示例

[官方文档](https://developer.work.weixin.qq.com/document/path/91770#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E7%BE%A4%E6%9C%BA%E5%99%A8%E4%BA%BA)

```python
from guolei_py3_qywx.webhook import Api as WebhookApi

webhook_api = WebhookApi(
    base_url="https://qyapi.weixin.qq.com/cgi-bin/webhook",
    key="your key"
)

# 发送文本信息
state = webhook_api.send_text(content="测试发送")
if state:
    print("发送成功")
```