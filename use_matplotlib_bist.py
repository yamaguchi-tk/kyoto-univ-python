#
# matplotlib でヒストグラムを描く
#
import matplotlib
#
# 出力先として tkinter を use で設定、pyplot のインポートより前に
#
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
#
# matplotlib で日本語表示を可能にする
# 使用環境で適当なもののコメントを外す
#
# For Windows
# matplotlib.rc('font', **{'family':'AppleGothic'})
# For Campus PC Terminal
# matplotlib.rc('font', **{'family':'IPAPGothic'})
# For macOS
matplotlib.rc('font', **{'family':'Hiragino Maru Gothic Pro'})
#
# ヒストグラムの作成
#
data = np.random.randn(1000)
plt.hist(data, bins=20)
#
# タイトル、軸ラベルを設定
#
plt.title('ヒストグラム')
plt.xlabel('データの値')
plt.ylabel('頻度')
#
# 表示
#
plt.show()
