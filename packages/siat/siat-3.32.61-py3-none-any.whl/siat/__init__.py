# -*- coding: utf-8 -*-
"""
功能：一次性引入SIAT的所有模块
作者：王德宏，北京外国语大学国际商学院
版权：2021-2025(C) 仅限教学使用，商业使用需要授权
联络：wdehong2000@163.com
"""

#==============================================================================
#屏蔽所有警告性信息
import warnings; warnings.filterwarnings('ignore')
#==============================================================================
from siat.allin import *

import pkg_resources
current_version=pkg_resources.get_distribution("siat").version

print("  Successfully enabled siat v{}".format(current_version))
#==============================================================================
# 处理stooq.py修复问题：
# 改为在security_prices.py中使用monkey patch对stooq.py进行override
#==============================================================================
