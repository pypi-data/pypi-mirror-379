# coding:utf-8
#
# unike/data/KGEDataLoader.py
#
# created by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 16, 2024
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Apr 27, 2024
#
# 为 KGE 模型读取数据.

"""
KGEDataLoader - KGE 模型读取数据集类。
"""

import typing
from .UniSampler import UniSampler
from .BernSampler import BernSampler
from .RGCNSampler import RGCNSampler
from .CompGCNSampler import CompGCNSampler
from .TestSampler import TestSampler
from .TradTestSampler import TradTestSampler
from torch.utils.data import DataLoader

class KGEDataLoader:

    """KGE 模型数据加载器。

    例子::

        from unike.data import KGEDataLoader, BernSampler, TradTestSampler

        dataloader = KGEDataLoader(
        	in_path = "../../benchmarks/FB15K/", 
        	batch_size = 8192,
        	neg_ent = 25,
        	test = True,
        	test_batch_size = 256,
        	num_workers = 16,
        	train_sampler = BernSampler,
        	test_sampler = TradTestSampler
        )
    """
    
    def __init__(
        self,
        in_path: str = "./",
        ent_file: str = "entity2id.txt",
        rel_file: str = "relation2id.txt",
        train_file: str = "train2id.txt",
        valid_file: str = "valid2id.txt",
        test_file: str = "test2id.txt",
        batch_size: int | None = None,
        neg_ent: int = 1,
        test: bool = False,
        test_batch_size: int | None = None,
        type_constrain: bool = True,
        num_workers: int | None = None,
        train_sampler: typing.Union[typing.Type[UniSampler], typing.Type[BernSampler], typing.Type[RGCNSampler], typing.Type[CompGCNSampler]] = BernSampler,
        test_sampler: typing.Type[TestSampler] = TradTestSampler):

        """创建 KGEDataLoader 对象。

        :param in_path: 数据集目录
        :type in_path: str
        :param ent_file: entity2id.txt
        :type ent_file: str
        :param rel_file: relation2id.txt
        :type rel_file: str
        :param train_file: train2id.txt
        :type train_file: str
        :param valid_file: valid2id.txt
        :type valid_file: str
        :param test_file: test2id.txt
        :type test_file: str
        :param batch_size: batch size
        :type batch_size: int | None
        :param neg_ent: 对于每一个正三元组, 构建的负三元组的个数, 替换 entity；对于 CompGCN 不起作用。
        :type neg_ent: int
        :param test: 是否读取验证集和测试集
        :type test: bool
        :param test_batch_size: test batch size
        :type test_batch_size: int | None
        :param type_constrain: 是否报告 type_constrain.txt 限制的测试结果
        :type type_constrain: bool
        :param num_workers: 加载数据的进程数
        :type num_workers: int
        :param train_sampler: 训练数据采样器
        :type train_sampler: typing.Union[typing.Type[UniSampler], typing.Type[BernSampler], typing.Type[RGCNSampler], typing.Type[CompGCNSampler]]
        :param test_sampler: 测试数据采样器
        :type test_sampler: typing.Type[TestSampler]
        """

        #: 数据集目录
        self.in_path: str = in_path
        
        if not self.in_path.endswith('/'):
            self.in_path = self.in_path + '/'
        
        #: entity2id.txt
        self.ent_file: str = ent_file
        #: relation2id.txt
        self.rel_file: str = rel_file
        #: train2id.txt
        self.train_file: str = train_file
        #: valid2id.txt
        self.valid_file: str = valid_file
        #: test2id.txt
        self.test_file: str = test_file
        #: batch size
        self.batch_size: int = batch_size
        #: 对于每一个正三元组, 构建的负三元组的个数, 替换 entity；对于 CompGCN 不起作用。
        self.neg_ent: int = neg_ent
        #: 是否读取验证集和测试集
        self.test: bool = test
        #: test batch size
        self.test_batch_size: int = test_batch_size
        #: 是否报告 type_constrain.txt 限制的测试结果
        self.type_constrain: bool = type_constrain
        #: 加载数据的进程数
        self.num_workers: int = num_workers

        #: 训练数据采样器
        self.train_sampler: typing.Union[UniSampler, BernSampler, RGCNSampler, CompGCNSampler] = train_sampler(
            in_path=self.in_path,
            ent_file=self.ent_file,
            rel_file=self.rel_file,
            train_file=self.train_file,
            batch_size=self.batch_size,
            neg_ent=self.neg_ent
        )

        #: 训练集三元组
        self.data_train: list[tuple[int, int, int]] = self.train_sampler.get_train()
        
        self.validate_data_train()

        if self.test:
            #: 测试数据采样器
            self.test_sampler: TestSampler = test_sampler(
                sampler=self.train_sampler,
                valid_file=self.valid_file,
                test_file=self.test_file,
                type_constrain=type_constrain
            )
        
            #: 验证集三元组
            self.data_val: list[tuple[int, int, int]] = self.test_sampler.get_valid()
            #: 测试集三元组
            self.data_test: list[tuple[int, int, int]] = self.test_sampler.get_test()
            
            self.validate_data_test()
            
    def validate_data_train(self) -> None:
        """验证训练集中的实体和关系 id 是否合法。"""
        
        ent_tol = self.get_ent_tol()
        rel_tol = self.get_rel_tol()
        
        for h, r, t in self.data_train:
            if h >= ent_tol or r >= rel_tol or t >= ent_tol:
                raise ValueError(f"the entity id or relation id of train data is out of range: {h}, {r}, {t}")
    
    def validate_data_test(self) -> None:
        """验证测试集和验证集中的实体和关系 id 是否合法。"""
        
        ent_tol = self.get_ent_tol()
        rel_tol = self.get_rel_tol()
        
        for h, r, t in self.data_val:
            if h >= ent_tol or r >= rel_tol or t >= ent_tol:
                raise ValueError(f"the entity id or relation id of test data is out of range: {h}, {r}, {t}")
        for h, r, t in self.data_test:
            if h >= ent_tol or r >= rel_tol or t >= ent_tol:
                raise ValueError(f"the entity id or relation id of test data is out of range: {h}, {r}, {t}")
        
    def get_ent_tol(self) -> int:

        """返回实体个数。
        
        :returns: 实体个数
        :rtype: int
        """

        return self.train_sampler.ent_tol

    def get_rel_tol(self) -> int:

        """返回关系个数。
        
        :returns: 关系个数
        :rtype: int
        """

        return self.train_sampler.rel_tol

    def train_dataloader(self) -> DataLoader:

        """返回训练数据加载器。
        
        :returns: 训练数据加载器
        :rtype: torch.utils.data.DataLoader
        """

        return DataLoader(
            self.data_train,
            shuffle=True,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            pin_memory=True,
            drop_last=True,
            collate_fn=self.train_sampler.sampling,
        )
            
    def val_dataloader(self) -> DataLoader:

        """返回验证数据加载器。
        
        :returns: 验证数据加载器
        :rtype: torch.utils.data.DataLoader
        """

        return DataLoader(
            self.data_val,
            shuffle=False,
            batch_size=self.test_batch_size,
            num_workers=self.num_workers,
            pin_memory=True,
            collate_fn=self.test_sampler.sampling,
        )

    def test_dataloader(self) -> DataLoader:

        """返回测试数据加载器。
        
        :returns: 测试数据加载器
        :rtype: torch.utils.data.DataLoader"""
        
        return DataLoader(
            self.data_test,
            shuffle=False,
            batch_size=self.test_batch_size,
            num_workers=self.num_workers,
            pin_memory=True,
            collate_fn=self.test_sampler.sampling,
        )

def get_kge_data_loader_hpo_config() -> dict[str, dict[str, typing.Any]]:
    
    """返回 :py:class:`KGEDataLoader` 的默认超参数优化配置。
    
    默认配置为::
    
        parameters_dict = {
            'dataloader': {
                'value': 'KGEDataLoader'
            },
            'in_path': {
                'value': './'
            },
            'ent_file': {
                'value': 'entity2id.txt'
            },
            'rel_file': {
                'value': 'relation2id.txt'
            },
            'train_file': {
                'value': 'train2id.txt'
            },
            'valid_file': {
                'value': 'valid2id.txt'
            },
            'test_file': {
                'value': 'test2id.txt'
            },
            'batch_size': {
                'values': [512, 1024, 2048, 4096]
            },
            'neg_ent': {
                'values': [1, 4, 16, 64]
            },
            'test_batch_size': {
                'value': 30
            },
            'type_constrain': {
                'value': True
            },
            'num_workers': {
                'value': 16
            },
            'train_sampler': {
                'value': 'BernSampler'
            },
            'test_sampler': {
                'value': 'TradTestSampler'
            }
        }
    
    :returns: :py:class:`KGEDataLoader` 的默认超参数优化配置
    :rtype: dict[str, dict[str, typing.Any]]
    """
    
    parameters_dict = {
        'dataloader': {
            'value': 'KGEDataLoader'
        },
        'in_path': {
            'value': './'
        },
        'ent_file': {
            'value': 'entity2id.txt'
        },
        'rel_file': {
            'value': 'relation2id.txt'
        },
        'train_file': {
            'value': 'train2id.txt'
        },
        'valid_file': {
            'value': 'valid2id.txt'
        },
        'test_file': {
            'value': 'test2id.txt'
        },
        'batch_size': {
            'values': [512, 1024, 2048, 4096]
        },
        'neg_ent': {
            'values': [1, 4, 16, 64]
        },
        'test_batch_size': {
            'value': 30
        },
        'type_constrain': {
            'value': True
        },
        'num_workers': {
            'value': 16
        },
        'train_sampler': {
            'value': 'BernSampler'
        },
        'test_sampler': {
            'value': 'TradTestSampler'
        }
    }
    
    return parameters_dict