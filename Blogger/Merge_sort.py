import math
import random
from plotting import plot_array

def merge_arrays(left_marker,middle_marker,right_marker):
  
  # print('---',arr,left_marker,middle_marker,right_marker)
  
  i = j = 0
  k=left_marker
  array_1 = arr[left_marker:middle_marker+1]
  array_2 = arr[middle_marker+1:right_marker+1]
  
  # print(array_1,array_2)
  title = f'{array_1} {array_2}'
  while i<len(array_1) and j<len(array_2):
    if array_1[i]<array_2[j]:
      arr[k] = array_1[i]
      i += 1
    else:
      arr[k] = array_2[j]
      j += 1
    k += 1
    plot_array(arr,title=title)
  while i<len(array_1):
    arr[k] = array_1[i]
    i+=1
    k+=1
    plot_array(arr,title=title)
  while j<len(array_2):
    arr[k] = array_2[j]
    j+=1
    k+=1
    plot_array(arr,title=title)
  # print('*',arr,'*')

def draw_function(merge_sort_function):
  def inner(arr,left_marker,right_marker):
    # print("I am decorator. will draw the function")
    plot_array(arr)
    return merge_sort_function(arr,left_marker,right_marker)
  return inner

# @draw_function
def mergeSort(arr,left_marker,right_marker):
  if left_marker<right_marker:
    middle_marker = math.floor((left_marker+right_marker)/2)

    # debugging code
    # left_side = arr[left_marker:middle_marker+1]
    # right_side = arr[middle_marker+1:right_marker+1]
    # print(left_side,right_side)
    
    mergeSort(arr,left_marker,middle_marker)
    mergeSort(arr,middle_marker+1,right_marker)
    merge_arrays(left_marker,middle_marker,right_marker)
    
# arr = [15,8,7,4,3,14,1,5]

arr = list(range(20))
random.shuffle(arr)
print(arr)
input()
mergeSort(arr,0,len(arr)-1)
plot_array(arr,'Merge Sort Finished')
input()
print(arr)