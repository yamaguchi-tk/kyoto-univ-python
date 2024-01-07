# Show Card Images with tkinter
import tkinter as tk

# カードファイル名を構成する要素
backs = ["blue", "green", "red"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "J", "Q", "K"]
joker = ["Joker"]

# カードファイル名を格納するリスト
cardImages = []
# カード背面画像名
for b in backs:
  for i in range(1, 6):
    card = "cardBack_" + b + str(i) + ".png"
    cardImages.append(card)
#　カード表面画像名
for s in suits:
  for r in ranks:
    card = "card" + s + r + ".png"
    cardImages.append(card)
# ジョーカー画像名
cardImages.append("card" + joker[0] + ".png")

root = tk.Tk()

# 画像ファイルを順に読みオンで
# PhotoImageクラスのオブジェクトのリストを作る
cardImageWidgets = []
for i in cardImages:
  image = tk.PhotoImage(file= "cards/" + i)
  cardImageWidgets.append(image)

# 画像にアクセスする添字
cardIndex = 0

def back():
  '一つ手前の画像に戻るコールバック関数'
  global cardIndex
  cardIndex -= 1
  if cardIndex < 0:
    cardIndex = len(cardImageWidgets) - 1
  # ラベルのimage属性を切り替える
  l["image"] = cardImageWidgets[cardIndex]

def forward():
  '一つ先の画像に戻るコールバック関数'
  global cardIndex
  cardIndex += 1
  if cardIndex >= len(cardImageWidgets):
    cardIndex = 0
  l["image"] = cardImageWidgets[cardIndex]

f = tk.Frame(root)
f.pack()
# 戻るボタンと進むボタン
bb = tk.Button(f, text = "<", command = back)
bf = tk.Button(f, text = ">", command = forward)
# カード画像を表示するラベルウィジェット
l = tk.Label(f, text = "card")
bb.grid(row=0, column=0)
l.grid(row=0, column=1)
bf.grid(row=0, column=2)
#　最初の画像を設定
l["image"] = cardImageWidgets[cardIndex]

root.mainloop()
