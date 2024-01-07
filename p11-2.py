import tkinter as tk

# 計算機能のための変数とイベント用の関数定義

# 2項演算のモデル
# 入力中の数字
current_number = 0
# 第一項
first_term = 0
# 第二項
second_term = 0
# 結果
result = 0

def do_plus():
  "+キーが押された時の計算動作、第一項の設定と入力中の数字のクリア"
  global current_number
  global first_term
  global operation

  first_term = current_number
  current_number = 0
  operation = "+"

def do_sub():
  "-キーが押された時の計算動作、第一項の設定と入力中の数字のクリア"
  global current_number
  global first_term
  global operation

  first_term = current_number
  current_number = 0
  operation = "-"

def do_multi():
  "*キーが押された時の計算動作、第一項の設定と入力中の数字のクリア"
  global current_number
  global first_term
  global operation

  first_term = current_number
  current_number = 0
  operation = "*"

def do_div():
  "/キーが押された時の計算動作、第一項の設定と入力中の数字のクリア"
  global current_number
  global first_term
  global operation

  first_term = current_number
  current_number = 0
  operation = "/"

def do_eq():
  "=キーが押された時の計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
  global second_term
  global result
  global current_number
  second_term = current_number

  if operation == "+":
    result = first_term + second_term
  elif operation == "-":
    result = first_term - second_term
  elif operation == "*":
    result = first_term * second_term
  elif operation == "/":
    if second_term == 0:
      result = "error"
    else:
      result = first_term // second_term
  else:
    result = "error"

  current_number = 0

# 数字キーを一括処理する関数
def key(n):
  global current_number
  current_number = current_number * 10 + n
  show_number(current_number)

def clear():
  global current_number
  current_number = 0
  show_number(current_number)

def plus():
  do_plus()
  show_number(current_number)

def eq():
  do_eq()
  show_number(result)

def show_number(num):
  e.delete(0, tk.END)
  e.insert(0, str(num))

def sub():
  do_sub()
  show_number(current_number)

def multi():
  do_multi()
  show_number(current_number)

def div():
  do_div()
  show_number(current_number)

# tkinterでの画面の構成

root = tk.Tk()
f = tk.Frame(root)
f.grid()

# ウィジェットの作成

b1 = tk.Button(f, text='1', command=lambda:key(1), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b2 = tk.Button(f, text='2', command=lambda:key(2), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b3 = tk.Button(f, text='3', command=lambda:key(3), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b4 = tk.Button(f, text='4', command=lambda:key(4), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b5 = tk.Button(f, text='5', command=lambda:key(5), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b6 = tk.Button(f, text='6', command=lambda:key(6), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b7 = tk.Button(f, text='7', command=lambda:key(7), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b8 = tk.Button(f, text='8', command=lambda:key(8), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b9 = tk.Button(f, text='9', command=lambda:key(9), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
b0 = tk.Button(f, text='0', command=lambda:key(0), width=2, font=('Helvetica', 14), highlightbackground='#ffffff')
bc = tk.Button(f, text='C', command=clear, width=2, font=('Helvetica', 14), highlightbackground='#ff0000' )
bp = tk.Button(f, text='+', command=plus, width=2, font=('Helvetica', 14), highlightbackground='#00ff00' )
be = tk.Button(f, text='=', command=eq, width=2, font=('Helvetica', 14), highlightbackground='#00ff00' )

bs = tk.Button(f, text='-', command=sub, width=2, font=('Helvetica', 14), highlightbackground='#00ff00' )
bm = tk.Button(f, text='*', command=multi, width=2, font=('Helvetica', 14), highlightbackground='#00ff00' )
bd = tk.Button(f, text='/', command=div, width=2, font=('Helvetica', 14), highlightbackground='#00ff00' )


# Grid型じおメトリマネージャーによるウィジェットの割付


b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bc.grid(row=1, column=3)
be.grid(row=4, column=3)
bp.grid(row=2, column=3)

bs.grid(row=3, column=4)
bm.grid(row=2, column=4)
bd.grid(row=1, column=4)

# 数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0, column=0, columnspan=4)
clear()

#　ここからGUIがスタート
root.mainloop()
