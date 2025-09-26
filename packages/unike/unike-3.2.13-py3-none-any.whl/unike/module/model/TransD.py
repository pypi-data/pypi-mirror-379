# coding:utf-8
#
# unike/module/model/TransD.py
# 
# git pull from OpenKE-PyTorch by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on May 7, 2023
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Feb 25, 2023
# 
# 该头文件定义了 TransD.

"""
TransD - 自动生成映射矩阵，简单而且高效，是对 TransR 的改进。
"""

import torch
import typing
import torch.nn as nn
import torch.nn.functional as F
from .Model import Model
from typing_extensions import override

class TransD(Model):

	"""
	``TransD`` :cite:`TransD` 提出于 2015 年，自动生成映射矩阵，简单而且高效，是对 TransR 的改进。

	评分函数为:

	.. math::
	
		\parallel (\mathbf{r}_p \mathbf{h}_p^T + \mathbf{I})\mathbf{h} + \mathbf{r} - (\mathbf{r}_p \mathbf{t}_p^T + \mathbf{I})\mathbf{t} \parallel_{L_1/L_2}

	正三元组的评分函数的值越小越好，如果想获得更详细的信息请访问 :ref:`TransD <transd>`。

	例子::

		from unike.utils import WandbLogger
		from unike.data import KGEDataLoader, BernSampler, TradTestSampler
		from unike.module.model import TransD
		from unike.module.loss import MarginLoss
		from unike.module.strategy import NegativeSampling
		from unike.config import Trainer, Tester
		
		wandb_logger = WandbLogger(
			project="unike",
			name="TransD-FB15K237",
			config=dict(
				in_path = '../../benchmarks/FB15K237/',
				batch_size = 2048,
				neg_ent = 25,
				test = True,
				test_batch_size = 10,
				num_workers = 16,
				dim_e = 200,
				dim_r = 200,
				p_norm = 1,
				norm_flag = True,
				margin = 4.0,
				use_gpu = True,
				device = 'cuda:1',
				epochs = 1000,
				lr = 1.0,
				opt_method = 'sgd',
				valid_interval = 100,
				log_interval = 100,
				save_interval = 100,
				save_path = '../../checkpoint/transd.pth'
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
		transd = TransD(
			ent_tol = dataloader.get_ent_tol(),
			rel_tol = dataloader.get_rel_tol(),
			dim_e = config.dim_e, 
			dim_r = config.dim_r, 
			p_norm = config.p_norm, 
			norm_flag = config.norm_flag)
		
		# define the loss function
		model = NegativeSampling(
			model = transd, 
			loss = MarginLoss(margin = config.margin)
		)
		
		# test the model
		tester = Tester(model = transd, data_loader = dataloader, use_gpu = config.use_gpu, device = config.device)
		
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
		dim_e: int = 100,
		dim_r: int = 100,
		p_norm: int = 1,
		norm_flag: bool = True,
		margin: float | None = None):
		
		"""创建 TransD 对象。

		:param ent_tol: 实体的个数
		:type ent_tol: int
		:param rel_tol: 关系的个数
		:type rel_tol: int
		:param dim_e: 实体嵌入和实体投影向量的维度
		:type dim_e: int
		:param dim_r: 关系嵌入和关系投影向量的维度
		:type dim_r: int
		:param p_norm: 评分函数的距离函数, 按照原论文，这里可以取 1 或 2。
		:type p_norm: int
		:param norm_flag: 是否利用 :py:func:`torch.nn.functional.normalize` 对实体和关系嵌入的最后一维执行 L2-norm。
		:type norm_flag: bool
		:param margin: 当使用 ``RotatE`` :cite:`RotatE` 的损失函数 :py:class:`unike.module.loss.SigmoidLoss`，需要提供此参数，将 ``TransE`` :cite:`TransE` 的正三元组的评分由越小越好转化为越大越好，如果想获得更详细的信息请访问 :ref:`RotatE <rotate>`。
		:type margin: float
		"""

		super(TransD, self).__init__(ent_tol, rel_tol)
		
		#: 实体嵌入和实体投影向量的维度
		self.dim_e: int = dim_e
		#: 关系嵌入和关系投影向量的维度
		self.dim_r: int = dim_r
		#: 评分函数的距离函数, 按照原论文，这里可以取 1 或 2。
		self.p_norm: int = p_norm
		#: 是否利用 :py:func:`torch.nn.functional.normalize` 
		#: 对实体和关系嵌入向量的最后一维执行 L2-norm。
		self.norm_flag: bool = norm_flag

		#: 根据实体个数，创建的实体嵌入
		self.ent_embeddings: torch.nn.Embedding = nn.Embedding(self.ent_tol, self.dim_e)
		#: 根据关系个数，创建的关系嵌入
		self.rel_embeddings: torch.nn.Embedding = nn.Embedding(self.rel_tol, self.dim_r)
		#: 根据实体个数，创建的实体投影向量
		self.ent_transfer: torch.nn.Embedding = nn.Embedding(self.ent_tol, self.dim_e)
		#: 根据关系个数，创建的关系投影向量
		self.rel_transfer: torch.nn.Embedding = nn.Embedding(self.rel_tol, self.dim_r)

		if margin != None:
			#: 当使用 ``RotatE`` :cite:`RotatE` 的损失函数 :py:class:`unike.module.loss.SigmoidLoss`，需要提供此参数，将 ``TransE`` :cite:`TransE` 的正三元组的评分由越小越好转化为越大越好，如果想获得更详细的信息请访问 :ref:`RotatE <rotate>`。
			self.margin: torch.nn.parameter.Parameter = nn.Parameter(torch.Tensor([margin]))
			self.margin.requires_grad = False
			self.margin_flag: bool = True
		else:
			self.margin_flag: bool = False

		nn.init.xavier_uniform_(self.ent_embeddings.weight.data)
		nn.init.xavier_uniform_(self.rel_embeddings.weight.data)
		nn.init.xavier_uniform_(self.ent_transfer.weight.data)
		nn.init.xavier_uniform_(self.rel_transfer.weight.data)

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

		h, r, t = self.tri2emb(triples, negs, mode)
		h_transfer, r_transfer, t_transfer = self.tri2transfer(triples, negs, mode)
		h = self._transfer(h, h_transfer, r_transfer)
		t = self._transfer(t, t_transfer, r_transfer)
		score = self._calc(h, r, t)
		if self.margin_flag:
			return self.margin - score
		else:
			return score

	def tri2transfer(
		self,
		triples: torch.Tensor,
		negs: torch.Tensor = None,
		mode: str = 'single') -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:

		"""
		返回三元组对应的嵌入向量。
		
		:param triples: 正确的三元组
		:type triples: torch.Tensor
		:param negs: 负三元组类别
		:type negs: torch.Tensor
		:param mode: 模式
		:type triples: str
		:returns: 头实体、关系和尾实体的嵌入向量
		:rtype: tuple[torch.Tensor, torch.Tensor, torch.Tensor]
		"""
		
		if mode == "single":
			head_emb = self.ent_transfer(triples[:, 0]).unsqueeze(1)
			relation_emb = self.rel_transfer(triples[:, 1]).unsqueeze(1)
			tail_emb = self.ent_transfer(triples[:, 2]).unsqueeze(1)
			
		elif mode == "head-batch" or mode == "head_predict":
			if negs is None:
				head_emb = self.ent_transfer.weight.data.unsqueeze(0)
			else:
				head_emb = self.ent_transfer(negs)
				
			relation_emb = self.rel_transfer(triples[:, 1]).unsqueeze(1)
			tail_emb = self.ent_transfer(triples[:, 2]).unsqueeze(1)
			
		elif mode == "tail-batch" or mode == "tail_predict": 
			head_emb = self.ent_transfer(triples[:, 0]).unsqueeze(1)
			relation_emb = self.rel_transfer(triples[:, 1]).unsqueeze(1)
			
			if negs is None:
				tail_emb = self.ent_transfer.weight.data.unsqueeze(0)
			else:
				tail_emb = self.ent_transfer(negs)
		
		return head_emb, relation_emb, tail_emb

	def _transfer(
		self,
		e: torch.Tensor,
		e_transfer: torch.Tensor,
		r_transfer: torch.Tensor) -> torch.Tensor:

		"""
		将头实体或尾实体的向量映射到关系向量空间。
		
		:param e: 头实体或尾实体向量。
		:type e: torch.Tensor
		:param e_transfer: 头实体或尾实体的投影向量
		:type e_transfer: torch.Tensor
		:param r_transfer: 关系的投影向量
		:type r_transfer: torch.Tensor
		:returns: 投影后的实体向量
		:rtype: torch.Tensor
		"""
	
		return F.normalize(
			self._resize(e, len(e.size())-1, r_transfer.size()[-1]) + torch.sum(e * e_transfer, -1, True) * r_transfer,
			p = 2, 
			dim = -1
		)

	def _resize(
		self,
		tensor: torch.Tensor,
		axis: int,
		size: int) -> torch.Tensor:

		"""计算实体向量与单位矩阵的乘法，并返回结果向量。

		源代码使用 :py:func:`torch.narrow` 进行缩小向量，
		:py:func:`torch.nn.functional.pad` 进行填充向量。
		
		:param tensor: 实体向量。
		:type tensor: torch.Tensor
		:param axis: 在哪个轴上进行乘法运算。
		:type axis: int
		:param size: 运算结果在 ``axis`` 上的维度大小，一般为关系向量的维度。
		:type size: int
		:returns: 乘法结果的向量
		:rtype: torch.Tensor
		"""

		shape = tensor.size()
		osize = shape[axis]
		if osize == size:
			return tensor
		if (osize > size):
			return torch.narrow(tensor, axis, 0, size)
		paddings = []
		for i in range(len(shape)):
			if i == axis:
				paddings = [0, size - osize] + paddings
			else:
				paddings = [0, 0] + paddings
		return F.pad(tensor, paddings, mode = "constant", value = 0)

	def _calc(
		self,
		h: torch.Tensor,
		r: torch.Tensor,
		t: torch.Tensor) -> torch.Tensor:

		"""计算 TransD 的评分函数。
		
		:param h: 头实体的向量。
		:type h: torch.Tensor
		:param r: 关系的向量。
		:type r: torch.Tensor
		:param t: 尾实体的向量。
		:type t: torch.Tensor
		:returns: 三元组的得分
		:rtype: torch.Tensor
		"""

		# 对嵌入的最后一维进行归一化
		if self.norm_flag:
			h = F.normalize(h, 2, -1)
			r = F.normalize(r, 2, -1)
			t = F.normalize(t, 2, -1)
		
		score = (h + r) - t
		
		# 利用距离函数计算得分
		score = torch.norm(score, self.p_norm, -1)
		return score

	@override
	def predict(
		self,
		data: dict[str, typing.Union[torch.Tensor,str]],
		mode: str) -> torch.Tensor:
		
		"""TransH 的推理方法。
		
		:param data: 数据。
		:type data: dict[str, typing.Union[torch.Tensor,str]]
		:param mode: 'head_predict' 或 'tail_predict'
		:type mode: str
		:returns: 三元组的得分
		:rtype: torch.Tensor
		"""

		triples = data["positive_sample"]
		h, r, t = self.tri2emb(triples, mode=mode)
		h_transfer, r_transfer, t_transfer = self.tri2transfer(triples, mode=mode)
		h = self._transfer(h, h_transfer, r_transfer)
		t = self._transfer(t, t_transfer, r_transfer)
		score = self._calc(h, r, t)

		if self.margin_flag:
			score = self.margin - score
			return score
		else:
			return -score

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
		pos_h, pos_r, pos_t = self.tri2emb(pos_sample)
		pos_h_transfer, pos_r_transfer, pos_t_transfer = self.tri2transfer(pos_sample)
		if mode == "bern":
			neg_h, neg_r, neg_t = self.tri2emb(neg_sample)
			neg_h_transfer, neg_r_transfer, neg_t_transfer = self.tri2transfer(neg_sample)
		else:
			neg_h, neg_r, neg_t = self.tri2emb(pos_sample, neg_sample, mode)
			neg_h_transfer, neg_r_transfer, neg_t_transfer = self.tri2transfer(pos_sample, neg_sample, mode)

		pos_regul = (torch.mean(pos_h ** 2) + 
					 torch.mean(pos_r ** 2) + 
					 torch.mean(pos_t ** 2) +
					 torch.mean(pos_h_transfer ** 2) + 
					 torch.mean(pos_r_transfer ** 2) +
					 torch.mean(pos_t_transfer ** 2)) / 6

		neg_regul = (torch.mean(neg_h ** 2) + 
					 torch.mean(neg_r ** 2) + 
					 torch.mean(neg_t ** 2) +
					 torch.mean(neg_h_transfer ** 2) + 
					 torch.mean(neg_r_transfer ** 2) +
					 torch.mean(neg_t_transfer ** 2)) / 6

		regul = (pos_regul + neg_regul) / 2

		return regul

def get_transd_hpo_config() -> dict[str, dict[str, typing.Any]]:

	"""返回 :py:class:`TransD` 的默认超参数优化配置。
	
	默认配置为::
	
		parameters_dict = {
			'model': {
				'value': 'TransD'
			},
			'dim_e': {
				'values': [50, 100, 200]
			},
			'dim_r': {
				'values': [50, 100, 200]
			},
			'p_norm': {
				'values': [1, 2]
			},
			'norm_flag': {
				'value': True
			}
		}

	:returns: :py:class:`TransD` 的默认超参数优化配置
	:rtype: dict[str, dict[str, typing.Any]]
	"""

	parameters_dict = {
		'model': {
			'value': 'TransD'
		},
		'dim_e': {
			'values': [50, 100, 200]
		},
		'dim_r': {
			'values': [50, 100, 200]
		},
		'p_norm': {
			'values': [1, 2]
		},
		'norm_flag': {
			'value': True
		}
	}
		
	return parameters_dict