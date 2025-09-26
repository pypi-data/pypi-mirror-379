# coding:utf-8
#
# unike/module/strategy/Strategy.py
#
# git pull from OpenKE-PyTorch by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on May 7, 2023
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 4, 2023
#
# 该脚本定义了损失函数的基类.

"""
Strategy - 该脚本定义了训练策略的基类。
"""

from ..BaseModule import BaseModule

class Strategy(BaseModule):

	"""
	继承自 :py:class:`unike.module.BaseModule`，什么额外的属性都没有增加。
	"""

	def __init__(self):
		
		"""创建 Loss 对象。"""
		
		super(Strategy, self).__init__()