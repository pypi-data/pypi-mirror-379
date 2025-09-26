# coding:utf-8
#
# unike/utils/Link.py
#
# created by wangtao <wangtao.cpu@gmail.com> on Jul 10, 2025
#
# 该脚本定义了 Link 类.

"""
Link - 链接分数计算。
"""

import torch
import pandas as pd
import os
from ..module.model import Model

class Link:
    """
    使用 KGE 模型对感兴趣的三元组计算链接分数。
    """
    def __init__(self,
                in_path: str = './',
                ent_file: str = "entity2id.txt", 
                rel_file: str = "relation2id.txt",
                all_file: str = "all2id.txt"):
        
        """创建 Link 对象。
        
        :param model: 模型
        :type model: Model
        :param in_path: 数据集目录
        :type in_path: str
        :param ent_file: entity2id.txt
        :type ent_file: str
        :param rel_file: relation2id.txt
        :type rel_file: str
        :param all_file: all2id.txt
        :type all_file: str
        """

        self.in_path = in_path
        self.ent_file = ent_file
        self.rel_file = rel_file
        self.all_file = all_file
        
        self.load_data()
        self.load_all()
        
        
    def load_data(self) -> None:
        
        """读取 :py:attr:`ent_file` 文件和 :py:attr:`rel_file` 文件。"""
        
        self.ent2id = {}
        self.id2ent = {}

        with open(os.path.join(self.in_path, self.ent_file)) as f:
            _ = (int)(f.readline())
            for line in f:
                entity, id_ = line.strip().split("\t")
                self.ent2id[entity] = int(id_)
                self.id2ent[int(id_)] = entity

        self.rel2id = {}
        self.id2rel = {}

        with open(os.path.join(self.in_path, self.rel_file)) as f:
            _ = (int)(f.readline())
            for line in f:
                relation, id_ = line.strip().split("\t")
                self.rel2id[relation] = int(id_)
                self.id2rel[int(id_)] = relation
    
    def load_all(self) -> None:
        
        """读取 :py:attr:`all_file` 文件。"""
        
        self.all = set()
        with open(os.path.join(self.in_path, self.all_file)) as f:
            _ = f.readline()
            for line in f:
                head, tail, rel = line.strip().split()
                self.all.add((int(head), int(rel), int(tail)))
        
        
    def link(self, 
             head_ids: list[int], 
             rel_ids: list[int], 
             tail_ids: list[int], 
             model: Model, 
             device: str = 'cpu'
        ) -> pd.DataFrame:
        
        """对给定的头实体、关系和尾实体进行组合并使用模型计算链接分数。
        
        :param head_ids: 头实体列表
        :type head_ids: list[int]
        :param rel_ids: 关系列表
        :type rel_ids: list[int]
        :param tail_ids: 尾实体列表
        :type tail_ids: list[int]
        :param device: 模型
        :type device: Model
        :param device: 设备
        :type device: str
        :returns: 结果数据框
        :rtype: pd.DataFrame
        """
        
        head_ids_ = torch.tensor(head_ids).long().to(device)
        rel_ids_ = torch.tensor(rel_ids).long().to(device)
        tail_ids_ = torch.tensor(tail_ids).long().to(device)

        triples = []
        scores = []
        
        model.eval()
        model.to(device)
        with torch.no_grad():
            for h_idx in range(len(head_ids_)):
                for r_idx in range(len(rel_ids_)):
                    h_id = head_ids_[h_idx]
                    r_id = rel_ids_[r_idx]
                    
                    h_id = h_id.tile((tail_ids_.shape[0], ))
                    r_id = r_id.tile((tail_ids_.shape[0], ))
                    
                    triple = torch.stack((h_id, r_id, tail_ids_)).T
                    data = {
                        "positive_sample": triple
                    }
                    score = model.predict(data, "single")
                    
                    scores.append(score)
                    triples.append(triple)
        
        triples = torch.cat(triples)
        scores = torch.cat(scores)
        
        sorted_scores, indices = torch.sort(scores.squeeze(), descending=True)
        sorted_triples = triples[indices]

        df = pd.DataFrame(sorted_triples.tolist(), columns=["head", "rel", "tail"])
        df["score"] = sorted_scores.tolist()
        df["in"] = df.apply(lambda row: (row['head'], row['rel'], row['tail']) in self.all, axis=1)
        df["head_ent"] = df["head"].map(self.id2ent)
        df["rel_ent"] = df["rel"].map(self.id2rel)
        df["tail_ent"] = df["tail"].map(self.id2ent)
        
        return df
