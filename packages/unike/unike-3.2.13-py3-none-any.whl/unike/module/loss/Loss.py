# coding:utf-8
#
# unike/module/loss/Loss.py
#
# git pull from OpenKE-PyTorch by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on May 7, 2023
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 4, 2023
#
# 该脚本定义了损失函数的基类.

"""
Loss - 该脚本定义了损失函数的基类。
"""

from ..BaseModule import BaseModule

class Loss(BaseModule):

	"""
	继承自 :py:class:`unike.module.BaseModule`，什么额外的属性都没有增加。
	"""

	def __init__(self):
		
		"""创建 Loss 对象。"""

		super(Loss, self).__init__()