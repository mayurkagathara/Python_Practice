import matplotlib.pyplot as plt
import random
fig = plt.figure()
ax = fig.add_subplot(111)

def plot_array(arr,title='title',no_of_comparison=0,no_of_swaps=0):
  ax.bar(list(range(0,len(arr))),arr,tick_label=arr)
  ax.set_title(title)
  data = f'Comparisons = {no_of_comparison}\n Swaps = {no_of_swaps}'
  ax.text(0,40,data)
  fig.canvas.draw()
  fig.canvas.flush_events()
  plt.pause(0.00001)
  ax.clear()

# Below code is for experimentation

# arr = list(range(10))
# random.shuffle(arr)
# title = 'Test graph'
# no_of_comparison = 0
# no_of_swaps = 0

# ax.bar(list(range(0,len(arr))),arr,tick_label=arr)
# ax.set_title(title)
# data = f'Comparisons = {no_of_comparison}\n Swaps = {no_of_swaps}'
# ax.text(0,40,data)
# fig.canvas.draw()
# fig.canvas.flush_events()
# plt.pause(0.00001)
# input()
# ax.clear()