import matplotlib.pyplot as plt
import pandas as pd

def plot_data(data, x_col, y_col, plot_type='line', title='Data Plot'):
    """绘制数据图表
    
    Args:
        data: DataFrame或DataProcessor实例
        x_col: x轴列名
        y_col: y轴列名
        plot_type: 图表类型，'line'或'bar'
        title: 图表标题
    """
    # 支持直接传入DataProcessor实例
    if hasattr(data, 'df') and isinstance(data.df, pd.DataFrame):
        df = data.df
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        raise ValueError("数据必须是DataFrame或DataProcessor实例")
    
    plt.figure(figsize=(10, 6))
    
    if plot_type == 'line':
        plt.plot(df[x_col], df[y_col])
    elif plot_type == 'bar':
        plt.bar(df[x_col], df[y_col])
    else:
        raise ValueError("不支持的图表类型")
    
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.grid(True)
    plt.show()
