import re

from loguru import logger
from wcferry import client

from utils.database import BotDatabase
from utils.plugin_interface import PluginInterface
from wcferry_helper import XYBotWxMsg

# 适配 XYBot v2.0.0

# 这里的类名得与插件设置文件中 plugin_name 一样。建议也与文件名一样
class my_command_plugin(PluginInterface):
    def __init__(self):
        config_path = 'plugins/my_command_plugin.yml'
        with open(config_path, 'r', encoding='utf-8') as f:  # 读取插件设置
            config = yaml.safe_load(f.read())

        # 这里从.yml文件中读取设置
        self.plugin_setting = config['plugin_setting']

        # 实例化机器人数据库类
        self.db = BotDatabase()

    async def run(self, bot: client.Wcf, recv: XYBotWxMsg):
        recv.content = re.split(" |\u2005", recv.content)  # 拆分消息

        nickname = self.db.get_nickname(recv.sender) # 获取发送者昵称

        message = f"Hey {nickname}! {self.plugin_setting}"

        logger.info(f'[发送信息]{message}| [发送到] {recv.roomid}')
        bot.send_text(message, recv.roomid)
