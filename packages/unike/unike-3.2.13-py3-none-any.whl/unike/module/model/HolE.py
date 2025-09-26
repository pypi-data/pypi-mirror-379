# coding:utf-8
#
# unike/module/model/HolE.py
# 
# git pull from OpenKE-PyTorch by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on May 7, 2023
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 31, 2024
# 
# 该头文件定义了 HolE.

"""
HolE - 利用循环相关进行知识图谱嵌入，是 RESCAL 的压缩版本，因此非常容易的应用于大型的知识图谱。
"""

import torch
import typing
import torch.nn as nn
from .Model import Model
from typing_extensions import override

class HolE(Model):

	"""
	``HolE`` :cite:`HolE` 提出于 2016 年，利用循环相关进行知识图谱嵌入，是 RESCAL 的压缩版本，因此非常容易的应用于大型的知识图谱。

	评分函数为:

	.. math::
	
		\mathbf{r}^T (\mathcal{F}^{-1}(\overline{\mathcal{F}(\mathbf{h})} \odot \mathcal{F}(\mathbf{t})))
	
	其中 :math:`\mathcal{F}(\cdot)` 和 :math:`\mathcal{F}^{-1}(\cdot)` 表示快速傅里叶变换，:math:`\overline{\mathbf{x}}` 表示复数共轭，:math:`\odot` 表示哈达玛积。
	
	正三元组的评分函数的值越大越好，负三元组越小越好，如果想获得更详细的信息请访问 :ref:`HolE <hole>`。

	例子::

		from unike.utils import WandbLogger
		from unike.data import KGEDataLoader, BernSampler, TradTestSampler
		from unike.module.model import HolE
		from unike.module.loss import SoftplusLoss
		from unike.module.strategy import NegativeSampling
		from unike.config import Trainer, Tester
		
		wandb_logger = WandbLogger(
			project="unike",
			name="HolE-WN18RR",
			config=dict(
				in_path = '../../benchmarks/WN18RR/',
				batch_size = 8192,
				neg_ent = 25,
				test = True,
				test_batch_size = 256,
				num_workers = 16,
				dim = 100,
				regul_rate = 1.0,
				use_gpu = True,
				device = 'cuda:0',
				epochs = 1000,
				lr = 0.5,
				opt_method = 'adagrad',
				valid_interval = 100,
				log_interval = 100,
				save_interval = 100,
				save_path = '../../checkpoint/hole.pth'
			)
		)
		
		config = wandb_logger.config
		
		# dataloader for training
		dataloader = KGEDataLoader(
			in_path = config.in_path, 
			batch_size = config.batch_size,
			neg_ent = config.neg_ent,
			test = config.test,
			test_batch_size = config.test_batch_size,
			num_workers = config.num_workers,
			train_sampler = BernSampler,
			test_sampler = TradTestSampler
		)
		
		# define the model
		hole = HolE(
			ent_tol = dataloader.get_ent_tol(),
			rel_tol = dataloader.get_rel_tol(),
			dim = config.dim
		)
		
		# define the loss function
		model = NegativeSampling(
			model = hole, 
			loss = SoftplusLoss(),
			regul_rate = config.regul_rate
		)
		
		# test the model
		tester = Tester(model = hole, data_loader = dataloader, use_gpu = config.use_gpu, device = config.device)
		
		# train the model
		trainer = Trainer(model = model, data_loader = dataloader.train_dataloader(), epochs = config.epochs,
			lr = config.lr, opt_method = config.opt_method, use_gpu = config.use_gpu, device = config.device,
			tester = tester, test = config.test, valid_interval = config.valid_interval,
			log_interval = config.log_interval, save_interval = config.save_interval,
			save_path = config.save_path, wandb_logger = wandb_logger)
		trainer.run()
		
		# close your wandb run
		wandb_logger.finish()
	"""

	def __init__(
		self,
		ent_tol: int,
		rel_tol: int,
		dim: int = 100):

		"""创建 HolE 对象。

		:param ent_tol: 实体的个数
		:type ent_tol: int
		:param rel_tol: 关系的个数
		:type rel_tol: int
		:param dim: 实体和关系嵌入向量的维度
		:type dim: int
		"""

		super(HolE, self).__init__(ent_tol, rel_tol)

		#: 实体和关系嵌入向量的维度
		self.dim: int = dim

		#: 根据实体个数，创建的实体嵌入
		self.ent_embeddings: torch.nn.Embedding = nn.Embedding(self.ent_tol, self.dim)
		#: 根据关系个数，创建的关系嵌入
		self.rel_embeddings: torch.nn.Embedding = nn.Embedding(self.rel_tol, self.dim)

		nn.init.xavier_uniform_(self.ent_embeddings.weight.data)
		nn.init.xavier_uniform_(self.rel_embeddings.weight.data)

	@override
	def forward(
		self,
		triples: torch.Tensor,
		negs: torch.Tensor = None,
		mode: str = 'single') -> torch.Tensor:

		"""
		定义每次调用时执行的计算。
		:py:class:`torch.nn.Module` 子类必须重写 :py:meth:`torch.nn.Module.forward`。
		
		:param triples: 正确的三元组
		:type triples: torch.Tensor
		:param negs: 负三元组类别
		:type negs: torch.Tensor
		:param mode: 模式
		:type triples: str
		:returns: 三元组的得分
		:rtype: torch.Tensor
		"""

		head_emb, relation_emb, tail_emb = self.tri2emb(triples, negs, mode)
		score = self._calc(head_emb, relation_emb, tail_emb)
		return score

	def _calc(
		self,
		h: torch.Tensor,
		r: torch.Tensor,
		t: torch.Tensor) -> torch.Tensor:

		"""计算 HolE 的评分函数。
		
		:param h: 头实体的向量。
		:type h: torch.Tensor
		:param r: 关系的向量。
		:type r: torch.Tensor
		:param t: 尾实体的向量。
		:type t: torch.Tensor
		:returns: 三元组的得分
		:rtype: torch.Tensor
		"""

		score = self._ccorr(h, t) * r
		score = torch.sum(score, -1)
		return score

	def _ccorr(
		self,
		a: torch.Tensor,
		b: torch.Tensor) -> torch.Tensor:

		"""计算循环相关 :math:`\mathcal{F}^{-1}(\overline{\mathcal{F}(\mathbf{h})} \odot \mathcal{F}(\mathbf{t}))`。
		
		利用 :py:func:`torch.fft.rfft` 计算实数到复数离散傅里叶变换，:py:func:`torch.fft.irfft` 是其逆变换；
		利用 :py:func:`torch.conj` 计算复数的共轭。

		:param a: 头实体的向量。
		:type a: torch.Tensor
		:param b: 尾实体的向量。
		:type b: torch.Tensor
		:returns: 返回循环相关计算结果。
		:rtype: torch.Tensor
		"""
		
		# 计算傅里叶变换
		a_fft = torch.fft.rfft(a, dim=-1)
		b_fft = torch.fft.rfft(b, dim=-1)
		
		# 复数的共轭
		a_fft = torch.conj(a_fft)
		
		# 哈达玛积
		p_fft = a_fft * b_fft
    	
		# 傅里叶变换的逆变换
		return torch.fft.irfft(p_fft, n=a.shape[-1], dim=-1)

	@override
	def predict(
		self,
		data: dict[str, typing.Union[torch.Tensor,str]],
		mode) -> torch.Tensor:
		
		"""HolE 的推理方法。
		
		:param data: 数据。
		:type data: dict[str, typing.Union[torch.Tensor,str]]
		:returns: 三元组的得分
		:rtype: torch.Tensor
		"""

		triples = data["positive_sample"]
		head_emb, relation_emb, tail_emb = self.tri2emb(triples, mode=mode)
		score = self._calc(head_emb, relation_emb, tail_emb)
		return score

	def regularization(
		self,
		data: dict[str, typing.Union[torch.Tensor, str]]) -> torch.Tensor:

		"""L2 正则化函数（又称权重衰减），在损失函数中用到。
		
		:param data: 数据。
		:type data: dict[str, typing.Union[torch.Tensor, str]]
		:returns: 模型参数的正则损失
		:rtype: torch.Tensor
		"""

		pos_sample = data["positive_sample"]
		neg_sample = data["negative_sample"]
		mode = data["mode"]
		pos_head_emb, pos_relation_emb, pos_tail_emb = self.tri2emb(pos_sample)
		if mode == "bern":
			neg_head_emb, neg_relation_emb, neg_tail_emb = self.tri2emb(neg_sample)
		else:
			neg_head_emb, neg_relation_emb, neg_tail_emb = self.tri2emb(pos_sample, neg_sample, mode)

		pos_regul = (torch.mean(pos_head_emb ** 2) + 
					 torch.mean(pos_relation_emb ** 2) + 
					 torch.mean(pos_tail_emb ** 2)) / 3

		neg_regul = (torch.mean(neg_head_emb ** 2) + 
					 torch.mean(neg_relation_emb ** 2) + 
					 torch.mean(neg_tail_emb ** 2)) / 3

		regul = (pos_regul + neg_regul) / 2

		return regul

	def l3_regularization(self) -> torch.Tensor:

		"""L3 正则化函数，在损失函数中用到。

		:returns: 模型参数的正则损失
		:rtype: torch.Tensor
		"""
		
		return (self.ent_embeddings.weight.norm(p = 3)**3 + self.rel_embeddings.weight.norm(p = 3)**3)

def get_hole_hpo_config() -> dict[str, dict[str, typing.Any]]:

	"""返回 :py:class:`HolE` 的默认超参数优化配置。
	
	默认配置为::
	
		parameters_dict = {
			'model': {
				'value': 'HolE'
			},
			'dim': {
				'values': [50, 100, 200]
			}
		}

	:returns: :py:class:`HolE` 的默认超参数优化配置
	:rtype: dict[str, dict[str, typing.Any]]
	"""

	parameters_dict = {
		'model': {
			'value': 'HolE'
		},
		'dim': {
			'values': [50, 100, 200]
		}
	}
		
	return parameters_dict