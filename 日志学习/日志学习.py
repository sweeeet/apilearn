"""
#29-30集

logging模块
0、日志名称
1、日志级别(level)：DEBUG,INFO,WAERNING,CRITICAL(FATAL)
2、输入渠道(handle)：控制台(StreamHandle)、文件(FileHandle)。
3、日志内容（Format）：时间-哪个文件-哪行代码-输出内容

logging模块，默认的root日志收集器，默认输出级别是warning


第一步：
创建一个日志收集器:logging.getLogger("收集器的名字")

第二部：
给日志收集器设置日志级别：logger.setLevel(logging.INFO)

第三步：
给日志收集器，创建一个输出渠道：handle1 = logging.StreamHandler()

第四步：
给渠道设置一个日志输出内容的格式

第五步：
将设置的格式，绑定到渠道当中，将格式与渠道关联起来

第六步：
将设置好的渠道，添加到日志收集器中
"""

import logging

# logging.info("hello 第一次日志输出操作")
# logging.warning("第一次警告级别的输出")

logger = logging.getLogger("nmb-py30")
# 设置日志输出级别
logger.setLevel(logging.INFO)
# 设置日志输出在哪些渠道
handle1 = logging.StreamHandler()
handle1.setLevel(logging.ERROR)
# 设置渠道的内容输出格式
fmt = '%(asctime)s - %(name)s - %(levelname)s -%(filename)s- %(lineno)d -%(message)s'
formatter = logging.Formatter(fmt)
# 将日志格式绑定到渠道中
handle1.setFormatter(formatter)
# 将设置好的渠道，添加到日志收集器中
logger.addHandler(handle1)
logger.info("11111")
logger.error("这个是个error")
