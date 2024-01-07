# 簡単な　tkinter の例、曜日をボタンで前後させて表示する
import tkinter as tk
# 曜日のリストと現在の表示を表す番号
dow = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
current_dow = 0

# 曜日を前に進める call back 関数
def forward():
  global current_dow
  current_dow += 1
  if current_dow == 7:
    current_dow = 0
  l_dow["text"] = dow[current_dow]

# 曜日を後ろに戻す call back 関数
def backward():
  global current_dow
  current_dow -= 1
  if current_dow == -1:
    current_dow = 6
  l_dow["text"] = dow[current_dow]

# tkinter を終了させる call bak　関数
def fin():
  root.destroy()

# ウィンドウとウィジェットの生成とウィジェットの配置
root = tk.Tk()
f = tk.Frame(root)
f.grid()
#
l_dow = tk.Label(f, text=dow[current_dow])
l_dow.grid(row=0, column=0, columnspan=3)
#
b_backward = tk.Button(f, text="<-", command = backward)
b_forward = tk.Button(f, text="->", command = forward)
b_exit = tk.Button(f, text="EXIT", command = fin)
b_backward.grid(row=1, column=0)
b_forward.grid(row=1, column=1)
b_exit.grid(row=1, column=2)
# GUI のスタート
print("tkinter started")
root.mainloop()
# GUI の終了の確認
print("tkinter stopped")
