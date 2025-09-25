import pandas as pd

class DataProcessor:
    """数据处理工具类"""
    
    def __init__(self, data=None):
        """初始化数据处理器
        
        Args:
            data: 可以是字典、列表或pandas DataFrame
        """
        if data is None:
            self.df = pd.DataFrame()
        elif isinstance(data, pd.DataFrame):
            self.df = data
        else:
            self.df = pd.DataFrame(data)
    
    def load_from_csv(self, file_path):
        """从CSV文件加载数据"""
        self.df = pd.read_csv(file_path)
        return self
    
    def get_summary(self):
        """获取数据摘要统计"""
        return self.df.describe()
    
    def handle_missing_values(self):
        """处理缺失值"""
        self.df = self.df.fillna(self.df.mean())
        return self
