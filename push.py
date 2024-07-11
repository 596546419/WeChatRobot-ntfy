import requests
import json


def push(msg_sender: str, msg_content: str) -> bool:
    """推送消息"""
    try:
        requests.post("http://acezy.top:8087/",
            data=json.dumps({
                "topic": "wechat",
                "title": msg_sender,
                "icon" : "https://open.weixin.qq.com/zh_CN/htmledition/res/assets/res-design-download/icon64_appwx_logo.png",
                "message": msg_content
            })
        )
        return True
    except Exception as e:
        return False