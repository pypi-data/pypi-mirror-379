# coding:utf-8
#
# unike/data/RevSampler.py
#
# created by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 15, 2024
# updated by LuYF-Lemon-love <luyanfeng_nlp@qq.com> on Jan 16, 2024
#
# 为 KGReader 增加相反关系，用于图神经网络模型.

"""
RevSampler - 为 KGReader 增加相反关系，用于图神经网络模型。
"""

import os
from .KGReader import KGReader

class RevSampler(KGReader):
    
    """在训练集中增加相反关系.

    对于每一个三元组 (h, r, t)，生成相反关系三元组 (t, r`, h): r` = r + rel_tol。
    """
    
    def __init__(
        self,
        in_path: str = "./",
        ent_file: str = "entity2id.txt",
        rel_file: str = "relation2id.txt",
        train_file: str = "train2id.txt"):

        """创建 RevSampler 对象。

        :param in_path: 数据集目录
        :type in_path: str
        :param ent_file: entity2id.txt
        :type ent_file: str
        :param rel_file: relation2id.txt
        :type rel_file: str
        :param train_file: train2id.txt
        :type train_file: str
        """
        
        super().__init__(
            in_path=in_path,
            ent_file=ent_file,
            rel_file=rel_file,
            train_file=train_file
        )

        self.add_reverse_relation()
        self.add_train_reverse_triples()
        self.get_hr2t_rt2h_from_train()
        
    def add_reverse_relation(self):

        """增加相反关系：r` = r + rel_tol"""
        
        with open(os.path.join(self.in_path, self.rel_file)) as f:
            f.readline()
            for line in f:
                relation, rid = line.strip().split("\t")
                self.rel2id[relation + "_reverse"] = int(rid) + self.rel_tol
                self.id2rel[int(rid) + self.rel_tol] = relation + "_reverse"
        self.rel_tol = len(self.rel2id)
        
    def add_train_reverse_triples(self):

        """对于每一个三元组 (h, r, t)，生成相反关系三元组 (t, r`, h): r` = r + rel_tol。"""

        tol = int(self.rel_tol / 2)
        
        with open(os.path.join(self.in_path, self.train_file)) as f:
            f.readline()
            for line in f:
                h, t, r = line.strip().split()
                self.train_triples.append(
                    (int(t), int(r) + tol, int(h))
                )