import os

import pywxdll
import yaml
from loguru import logger

from plugin_interface import PluginInterface


# 这里的类名得与插件设置文件中 plugin_name 一样。建议也与文件名一样
class my_plugin(PluginInterface):
    def __init__(self):
        config_path = os.path.abspath(__file__)[:-3] + '.yml'
        with open(config_path, 'r', encoding='utf-8') as f:  # 读取插件设置
            config = yaml.load(f.read(), Loader=yaml.FullLoader)

        # 这里从.yml文件中读取设置
        self.plugin_setting = config['plugin_setting']

        # 这里从主设置中读取微信机器人api的ip地址、端口，并启动
        current_directory = os.path.dirname(os.path.abspath(__file__))
        main_config_path = os.path.join(current_directory, '../main_config.yml')
        with open(main_config_path, 'r', encoding='utf-8') as f:  # 读取设置
            main_config = yaml.load(f.read(), Loader=yaml.FullLoader)

        self.ip = main_config['ip']  # ip
        self.port = main_config['port']  # 端口
        self.bot = pywxdll.Pywxdll(self.ip, self.port)  # 机器人api
        self.bot.start()  # 开启机器人

    def run(self, recv):  # 当用户指令与插件设置中关键词相同，执行对应插件的run函数
        out_message = 'hello,world! \n plugin_setting:{plugin_setting}'.format(
            plugin_setting=self.plugin_setting)  # 组建消息
        logger.info('[发送信息]{out_message}| [发送到] {wxid}'.format(out_message=out_message, wxid=recv['wxid']))
        self.bot.send_txt_msg(recv['wxid'], out_message)  # 发送消息，更多微信机器人api函数请看 https://github.com/HenryXiaoYang/pywxdll 中的文档
