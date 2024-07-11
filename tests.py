import unittest

from guolei_py3_qywx.webhook import Webhook


class MyTestCase(unittest.TestCase):
    def test_webhook(self):
        webhook = Webhook(
            base_url="https://qyapi.weixin.qq.com/cgi-bin/webhook",
            key="366095be-225c-4c92-9369-c9d9bc5cc1c5"
        )
        state = webhook.send_text(content="测试发送")
        if state:
            print("发送成功")
        self.assertTrue(state, "test failed")  # add assertion here


if __name__ == '__main__':
    unittest.main()
