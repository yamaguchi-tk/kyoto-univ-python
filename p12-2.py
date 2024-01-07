#
# tkinter canvas を使ったアナログ時計、ボタンあり
#
import tkinter as tk
import math
import time

#
# Frame を拡張したクラス
#
class MyFrame(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
#
# キャンバスの作成
#
    self.size = 200
    self.clock = tk.Canvas(self, width=self.size, height=self.size, background="white")
    self.clock.grid(row=0, column=0)
#
# 文字盤の描画
#
    self.font_size = int(self.size/15)
    for number in range(1, 12 + 1):
      x = self.size/2 + math.cos(math.radians(number*360/12 - 90))*self.size/2*0.85
      y = self.size/2 + math.sin(math.radians(number*360/12 - 90))*self.size/2*0.85
      self.clock.create_text(x,y,text=str(number), fill="black", font=("", 14))
#
# 日付表示をオンオフするボタンの作成
#
      self.b = tk.Button(self, text="Show Date", font=("", 14), command=self.toggle)
      self.b.grid(row=1, column=0)
#
# 秒針表示をオンオフするボタンの作成
#
      self.bsec = tk.Button(self, text="Show Sec", font=("", 14), command=self.toggle_sec)
      self.bsec.grid(row=1, column=1)

#
# 時刻の経過確認などの動作のためのインスタンス変数
#
      self.sec = time.localtime().tm_sec
      self.min = time.localtime().tm_min
      self.hour = time.localtime().tm_hour
      self.show_date = False
      self.show_sec = False
  
  #
  # ボタンが押された時の call back
  #
  def toggle(self):
    if self.show_date:
      self.b.configure(text="Show Date") 
    else:
      self.b.configure(text="Hide Date")
    self.show_date = not self.show_date

  def toggle_sec(self):
    if self.show_sec:
      self.bsec.configure(text="Show Sec") 
    else:
      self.bsec.configure(text="Hide Sec")
    self.show_sec = not self.show_sec

  #
  # 変化する画面の描画
  #
  def display(self):
    #
    # 秒針の描画
    #
    self.sec = time.localtime().tm_sec
    angle = math.radians(self.sec*360/60 - 90)
    x0 = self.size/2 - math.cos(angle)*self.size/2*0.1
    y0 = self.size/2 - math.sin(angle)*self.size/2*0.1
    x = self.size/2 + math.cos(angle)*self.size/2*0.75
    y = self.size/2 + math.sin(angle)*self.size/2*0.75
    #
    # 前の描画をタグで検索して消してから描画
    #
    self.clock.delete("SEC")
    self.clock.create_line(x0,y0,x,y, width=1, fill="red", tag="SEC")
    #
    # 分針、時針の描画、1分毎、時針は分まで考慮
    #
    x0 = self.size/2
    y0 = self.size/2
    self.min = time.localtime().tm_min
    angle = math.radians(self.min*360/60 - 90)
    x = self.size/2 + math.cos(angle)*self.size/2*0.65
    y = self.size/2 + math.sin(angle)*self.size/2*0.65
    self.clock.delete("MIN")
    self.clock.create_line(x0,y0,x,y, width=3, fill="blue", tag="MIN")
    
    self.hour = time.localtime().tm_hour
    x0 = self.size/2
    y0 = self.size/2
    angle = math.radians((self.hour%12+self.min/60)*360/12 - 90)
    x = self.size/2 + math.cos(angle)*self.size/2*0.55
    y = self.size/2 + math.sin(angle)*self.size/2*0.55
    self.clock.delete("HOUR")
    self.clock.create_line(x0,y0,x,y, width=3, fill="green", tag="HOUR")
    #
    # 日付の描画、秒が変わるか、ボタンが押された時
    #
    x = self.size/2
    y = self.size/2 + 20
    text = time.strftime('%Y/%m/%d %I:%M:%S(%p)')
    self.clock.delete("TIME")
    self.clock.create_text(x, y, text=text, font=("", 12), fill="black", tag="TIME")
    if self.show_date:
      self.clock.create_text(x, y, text=text, font=("", 12), fill="black", tag="TIME")
    if not self.show_sec:
      self.clock.delete("SEC")

    #
    # 100ミリ秒後に再度呼び出す
    #
    self.after(100, self.display)

root = tk.Tk()
f = MyFrame(root)
f.pack()
f.display()
root.mainloop()
