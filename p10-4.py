from turtle import *
def come(x, y):
  (xx, yy) = pos()
  newxy = ((xx + x) / 2, (yy + y) / 2)
  print(x, y)
  goto(newxy)
onescreenclick(come)
done()
