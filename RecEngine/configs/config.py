# -*- coding: utf-8 -*-
class Config(object):
    """保存可能需要的参数，并为其设置默认值"""
    
    def __init__(self):
        
        self.size = 0.8 #训练集大小
        self.factor = 10 #矩阵分解潜因子维度
        self.lr = 0.01 #学习速率
        self.maxIter = 100 #最大迭代次数
        self.k_fold_num = 5 #交叉验证折数
        self.sep = ','
        self.rating_cv_path = None
        self.dataset_name = None
        self.coldUserRating = 1 #评分数小于这个值的用户被判断为冷启动用户
        self.n = 10 #CF算法的近邻数
        self.verbose = True  #是否输出预测过程
        