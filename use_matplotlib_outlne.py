import matplotlib
# Set tkinter as the output destination before importing pyplot
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
# Enable matplotLib to display japanese characters
# Yu Gothic can be used in matplotlib version 3.1.0 or later
matplotlib.rc('font', **{'family':'AppleGothic'})
# For Mac User, try the following insted of the above line
# matplotlib.rc('font', **{'family':'Hiragino Maru Gothic Pro'})
# The following is an example plot
data = [1,2,3]
plt.plot(data)
plt.title('タイトル')
plt.show()
