# ！__author__ =='wuwa'
# ! -*- utf-8 -*-

from common.readConfig import ReadConfig


def choice_env(envs):
    """
    选择测试环境
    :param envs:
    :return:
    """

    if'TEST' == envs:
        baseurl = ReadConfig().get_config_value('TESTHTTP', 'BASEURL')
    elif 'PRO' == envs:
        baseurl = ReadConfig().get_config_value('HTTP', 'BASEURL')
    else:
        print('请选择执行环境')
    return baseurl
