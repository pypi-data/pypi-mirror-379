from typing import Literal
import os

PROJECT_NAME = 'wxauto'

class WxParam:
    # 语言设置
    LANGUAGE: Literal['cn', 'cn_t', 'en'] = 'cn'

    # 是否启用日志文件
    ENABLE_FILE_LOGGER: bool = True

    # # 下载文件/图片默认保存路径
    # DEFAULT_SAVE_PATH: str = os.path.join(os.getcwd(), 'wx图片文件下载')

    # 以当前文件所在目录为基准，向上找项目根，再进入 tianxiadatong_wx_robot/wx图片文件下载
    _BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEFAULT_SAVE_PATH: str = os.path.join(_BASE_DIR, 'wx图片文件')

    # 是否启用消息哈希值用于辅助判断消息，开启后会稍微影响性能
    MESSAGE_HASH: bool = False

    # 头像到消息X偏移量，用于消息定位，点击消息等操作
    DEFAULT_MESSAGE_XBIAS = 51

    # 是否强制重新自动获取X偏移量，如果设置为True，则每次启动都会重新获取
    FORCE_MESSAGE_XBIAS: bool = False

    # 监听消息时间间隔，单位秒
    LISTEN_INTERVAL: int = 1

    # 搜索聊天对象超时时间
    SEARCH_CHAT_TIMEOUT: int = 5

class WxResponse(dict):
    def __init__(self, status: str, message: str, data: dict = None):
        super().__init__(status=status, message=message, data=data)

    def __str__(self):
        return str(self.to_dict())
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'status': self['status'],
            'message': self['message'],
            'data': self['data']
        }

    def __bool__(self):
        return self.is_success
    
    @property
    def is_success(self):
        return self['status'] == '成功'

    @classmethod
    # def success(cls, message=None, data: dict = None):
    #     return cls(status="成功", message=message, data=data)
    def success(cls, message: str = "", data=None):
        return cls(status="成功", message=message or "", data=data)

    @classmethod
    def failure(cls, message: str, data: dict = None):
        return cls(status="失败", message=message, data=data)

    @classmethod
    def error(cls, message: str, data: dict = None):
        return cls(status="错误", message=message, data=data)