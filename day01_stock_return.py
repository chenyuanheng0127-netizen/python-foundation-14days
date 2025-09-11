import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1.模拟价格序列
np.random.seed(42)
n = 1000
price = 100 + np.cumsum(np.random.normal(0, 1, n))  # 正态分布随机游走

#2.计算对数收益率
returns = np.diff(np.log(price))

#3.计算累计收益率
cumulative_returns = np.cumsum(returns) # 累积对数收益率

#4.pandas处理数据
df = pd.DataFrame({
    "Price": price[1:],  # 对应returns
    "Log Returns": returns
})
print(df.head())

#4.保存到csv
df.to_csv("day01_stock_return_data.csv", index=False)

#5.可视化
plt.figure(figsize=(8,4))
plt.subplot(2,1,1)
plt.plot(price, label="Price")
plt.legend()

plt.subplot(2,1,2)
plt.plot(returns, label="Log Returns", color="purple")
plt.legend()

plt.tight_layout()
plt.savefig("day01_stock_return.png")
plt.show()
