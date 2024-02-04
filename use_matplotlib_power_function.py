# Numpy のデータを　　plot する例題
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
# For Windows
# matplotlib.rc('font', **{'family':'AppleGothic'})
# For Campus PC Terminal
# matplotlib.rc('font', **{'family':'IPAPGothic'})
# For macOS
matplotlib.rc('font', **{'family':'Hiragino Maru Gothic Pro'})
#
# x の　1乗- 4乗をプロットする
#
steps = 100
order = 4
maxx = 2
#
# 要素の値 0 で steps 行、order 列の行列をさk末い
#
datalist = np.zeros((steps, order))
#
# 凡例用のリスト
#
legend_label=[]
#
# x の値を linespace で作成
#
x = np.linspace(0, maxx, steps)
#
# 各列について、一気に計算する
#
for  j in range(1, order+1):
  datalist[:, j-1] = x**j
  legend_label.append(str(j)+'乗')
#
# プロット
#
plt.plot(x, datalist)
plt.title('xのべき乗')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(legend_label)
plt.show()
