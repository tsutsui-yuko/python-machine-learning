import numpy as np
import ridge
import linearreg
import matplotlib.pyplot as plt

# y = 2x + 1 (0 ≦ x < 12)
x = np.arange(12)
y = 1 + 2 * x

# 異常値？を挿入
y[2] = 20
y[4] = 0

xmin = 0
xmax = 12
ymin = -1
ymax = 25
# 図形描画領域を2×5用意
fig, axes = plt.subplots(nrows=2, ncols=5)
for i in range(5):
    # 各グラフの描画領域を設定
    axes[0, i].set_xlim([xmin, xmax])
    axes[0, i].set_ylim([ymin, ymax])
    axes[1, i].set_xlim([xmin, xmax])
    axes[1, i].set_ylim([ymin, ymax])
    # 学習データの設定（iが増えるごとに二個ずつ増える）
    xx = x[:2 + i * 2]
    yy = y[:2 + i * 2]
    # 学習データの描画
    axes[0, i].scatter(xx, yy, color="k")
    axes[1, i].scatter(xx, yy, color="k")

    # 上半分の図に線形回帰で近似、結果を描画
    model = linearreg.LinearRegression()
    model.fit(xx, yy)
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
    axes[0, i].plot(xs, ys, color="k")

    # 下半分の図にリッジ回帰で近似、結果を描画。大げさに見えるようにλを10にしたっぽい
    model = ridge.RidgeRegression(10.)
    model.fit(xx, yy)
    xs = [xmin, xmax]
    ys = [model.w_[0] + model.w_[1] * xmin, model.w_[0] + model.w_[1] * xmax]
    axes[1, i].plot(xs, ys, color="k")

plt.show()

