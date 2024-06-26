from nonebot.plugin import PluginMetadata
from .stat_matchers import *
from .stat_monitors import *
from .stat_restful_api import *

__author__ = "snowykami"
__plugin_meta__ = PluginMetadata(
    name="统计信息",
    description="统计机器人的信息",
    usage=(
            "stat msg [limit] 查看统计次数内的消息\n"
            "stat msg -g|--group [group_id] 查看群的统计信息，不带参数为全群\n"
    ),
    type="application",
    homepage="https://github.com/snowykami/LiteyukiBot",
    extra={
            "liteyuki"      : True,
            "toggleable"    : False,
            "default_enable": True,
    }
)
