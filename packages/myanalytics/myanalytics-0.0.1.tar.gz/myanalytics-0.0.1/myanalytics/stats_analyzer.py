import numpy as np

def calculate_mean(data):
    """计算数据均值"""
    return np.mean(data)

def calculate_variance(data):
    """计算数据方差"""
    return np.var(data)

def calculate_correlation(x, y):
    """计算两组数据的相关系数"""
    if len(x) != len(y):
        raise ValueError("两组数据长度必须一致")
    return np.corrcoef(x, y)[0, 1]