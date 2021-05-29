import random
from plotting import plot_array

# %matplotlib inline
arr = list(range(50))
random.shuffle(arr)

# x = input()

no_of_comparison = 0
no_of_swaps = 0
for arr_index in range(1,len(arr)):
  no_of_comparison += 1

  plot_array(arr,title='insertion sort',no_of_comparison=no_of_comparison,no_of_swaps=no_of_swaps)
  number_to_put = arr[arr_index]
  left_index = arr_index - 1
  while left_index >= 0 and arr[left_index] > number_to_put:
    no_of_comparison += 1
    no_of_swaps += 1
    arr[left_index+1] = arr[left_index]
    arr[left_index] = number_to_put
    left_index -= 1
  # arr[left_index+1] = number_to_put  # OR you can put the number at last.
plot_array(arr,no_of_comparison=no_of_comparison,no_of_swaps=no_of_swaps)

y = input()