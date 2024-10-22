import re

from loguru import logger
from wcferry import client

from utils.database import BotDatabase
from utils.plugin_interface import PluginInterface
from wcferry_helper import XYBotWxMsg

# 适配 XYBot v2.0.0

# 这里的类名得与插件设置文件中 plugin_name 一样。建议也与文件名一样
class my_join_group_plugin(PluginInterface):
    def __init__(self):
        pass

    async def run(self, bot: client.Wcf, recv: XYBotWxMsg):
        logger.debug(f"收到入群消息！{recv.join_group} 入群了！")

        message = f"收到入群消息！{recv.join_group} 入群了！"
        bot.send_text(message, recv.roomid)
