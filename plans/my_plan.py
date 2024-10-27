import asyncio

import schedule
import yaml
from loguru import logger
from wcferry import client

from utils.plans_interface import PlansInterface


class my_plan(PlansInterface):
    def __init__(self):
        main_config_path = "main_config.yml"
        with open(main_config_path, "r", encoding="utf-8") as f:  # 读取设置
            main_config = yaml.safe_load(f.read())

        self.timezone = main_config["timezone"]  # 时区

    async def job(self, bot: client.Wcf):
        logger.info(f"每分钟执行一次, 设置时区: {self.timezone}")
        bot.send_text("每分钟执行一次", "filehelper")

    def job_async(self, bot: client.Wcf):
        loop = asyncio.get_running_loop()
        loop.create_task(self.job(bot))

    def run(self, bot: client.Wcf):
        schedule.every(1).minute.do(self.job_async, bot)  # 每分钟执行一次
