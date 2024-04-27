import pywxdll
import yaml
from loguru import logger

from plugin_interface import PluginInterface

# 适配 XYBot v0.0.6

# 这里的类名得与插件设置文件中 plugin_name 一样。建议也与文件名一样
class my_plugin(PluginInterface):
    def __init__(self):
        config_path = 'plugins/my_plugin.yml'
        with open(config_path, 'r', encoding='utf-8') as f:  # 读取插件设置
            config = yaml.safe_load(f.read())

        # 这里从.yml文件中读取设置
        self.plugin_setting = config['plugin_setting']

        # 这里从主设置中读取微信机器人api的ip地址、端口，并启动
        main_config_path = 'main_config.yml'  # 主设置文件路径
        with open(main_config_path, 'r', encoding='utf-8') as f:  # 读取设置
            main_config = yaml.safe_load(f.read())  # 读取设置

        self.ip = main_config['ip']  # ip
        self.port = main_config['port']  # 端口
        self.bot = pywxdll.Pywxdll(self.ip, self.port)  # 机器人api

    async def run(self, recv):  # 当用户指令与插件设置中关键词相同，执行对应插件的run函数
        out_message = 'hello,world! \n plugin_setting:{plugin_setting}'.format(
            plugin_setting=self.plugin_setting)  # 组建消息
        logger.info('[发送信息]{out_message}| [发送到] {wxid}'.format(out_message=out_message, wxid=recv['wxid']))
        self.bot.send_txt_msg(recv['wxid'],
                              out_message)  # 发送消息，更多微信机器人api函数请看 https://github.com/HenryXiaoYang/pywxdll 中的文档
