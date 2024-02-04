#
# subplot を使う例
#
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
#
# テキストで日本語を表示できるようにする
# 使用環境で適当なもののコメントを外す
# For Windows
# matplotlib.rc('font', **{'family':'AppleGothic'})
# For Campus PC Terminal
# matplotlib.rc('font', **{'family':'IPAPGothic'})
# For macOS
matplotlib.rc('font', **{'family':'Hiragino Maru Gothic Pro'})
#
#
# 3つの subplot を作成、間隔を調整
#
flg = plt.figure()
ax1 = flg.add_subplot(2,2,1)
ax2 = flg.add_subplot(2,2,2)
ax3 = flg.add_subplot(2,2,3)
plt.subplots_adjust(hspace=0.5, wspace=0.5)
#
# 1つめに線グラフを出力
#
data = np.random.randn(100).cumsum()
ax1.plot(data)
ax1.set_title('線グラフ')
ax1.set_xlabel('時間')
ax1.set_ylabel('場所')
#
# 2つめに散布図を出力
#
datax = np.random.randn(100)
datay = datax + np.random.randn(100) * 0.3
ax2.scatter(datax, datay, label='データ1')

datax = np.random.randn(100)
datay = 0.6 * datax + np.random.randn(100) * 0.3
ax2.scatter(datax, datay, color='red', label='データ2')

ax2.set_title('散布図')
ax2.set_xlabel('属性1')
ax2.set_ylabel('属性2')
ax2.legend()

#
# 3つめにヒストグラムを出力
#
data = np.random.randn(1000)
ax3.hist(data, bins=20)

ax3.set_title('ヒストグラム')
ax3.set_xlabel('データの値')
ax3.set_ylabel('頻度')

#
# グラフを表示
#
plt.show()
