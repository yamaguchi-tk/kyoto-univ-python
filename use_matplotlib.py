#
# matplotlib 基本の使い方
#
import matplotlib
#
# 出力先として tkinter を use で設定、pyplot のインポートより前に
#
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
#
# matplotlib で日本語表示を可能にする
# 使用環境で適当なもののコメントを外す
#
# For Windows
#matplotlib.rc('font', **{'family':'AppleGothic'})
# For Campus PC Terminal
# matplotlib.rc('font', **{'family':'IPAPGothic'})
# For macOS
matplotlib.rc('font', **{'family':'Hiragino Maru Gothic Pro'})
#
# 3本の棒グラフを表示する
#
plt.plot([1,2,3], 'k-', label='系列1')
plt.plot([2,3,4], 'r--', label='系列2')
plt.plot([3,4,5], 'b--o', label='系列3')
#
plt.title('タイトル')
plt.xlabel('横軸')
plt.ylabel('縦軸')
plt.legend() # 凡例
plt.show()
