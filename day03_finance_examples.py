import numpy as np

def simple_returns(prices: np.ndarray) -> np.ndarray:
    """
    简单收益率 r_t = P_t / P_{t-1} - 1
    prices: shape (T,)
    return: shape (T-1,)
    """
    # prices[1:] 与 prices[:-1] 自然对齐： [P1,P2,...,PT] / [P0,P1,...,P_{T-1}]
    return prices[1:] / prices[:-1] - 1

def log_returns(prices: np.ndarray) -> np.ndarray:
    """
    对数收益率 r_t = ln(P_t) - ln(P_{t-1}) = ln(P_t / P_{t-1})
    优点：可加性强，金融中常用
    """
    return np.diff(np.log(prices))

def zscore_by_column(X: np.ndarray) -> np.ndarray:
    """
    对二维数据按列做 z-score 标准化：
      Z = (X - mean_col) / std_col
    适用于：多资产特征按列标准化，方便比较
    """
    mu = X.mean(axis=0, keepdims=True)     # (1, n_features)
    sigma = X.std(axis=0, keepdims=True)   # (1, n_features)
    # 防止除零（极端情况列方差为0）
    sigma = np.where(sigma == 0, 1.0, sigma)
    return (X - mu) / sigma

def moving_average(prices: np.ndarray, window: int = 3) -> np.ndarray:
    """
    简单滑动平均（SMA），用卷积实现：
      MA_t = (1/k) * sum_{i=0..k-1} P_{t-i}
    mode='valid' 只保留能完整覆盖窗口的位置
    """
    weights = np.ones(window, dtype=np.float64) / window
    return np.convolve(prices, weights, mode='valid')

def demo_small_series():
    print("=== Demo: 1D 价格序列 ===")
    prices = np.array([100.0, 101.0, 102.5, 101.2, 103.0], dtype=np.float64)
    print("prices:", prices)

    ret = simple_returns(prices)
    print("simple returns:", ret)

    logret = log_returns(prices)
    print("log returns   :", logret)

    ma3 = moving_average(prices, window=3)
    print("3-day moving average:", ma3)

def demo_2d_features():
    print("\n=== Demo: 2D 特征矩阵（按列 z-score） ===")
    # 模拟 5 天 × 3 只股票的某些特征（如收益/成交量/动量…）
    np.random.seed(42)
    X = np.random.randn(5, 3) * 2 + np.array([0.0, 1.0, -1.0])  # 人为制造不同均值
    print("X:\n", X)

    Z = zscore_by_column(X)
    print("\nZ (z-score by column):\n", Z)

    # 验证每列 ~ 均值≈0、方差≈1
    mu = Z.mean(axis=0)
    std = Z.std(axis=0)
    print("\nZ column means ~ 0 :", mu)
    print("Z column stds  ~ 1 :", std)

if __name__ == "__main__":
    demo_small_series()
    demo_2d_features()

import matplotlib.pyplot as plt
   
prices = np.array([100.0, 101.0, 102.5, 101.2, 103.0], dtype=np.float64)
ma3 = moving_average(prices, window=3)
plt.plot(prices, label="price")
plt.plot(np.arange(2, 2 + len(ma3)), ma3, label="MA(3)")  # 对齐横坐标
plt.legend()
plt.title("Price vs 3-day Moving Average")
plt.show()