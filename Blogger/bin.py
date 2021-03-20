# i= [12,9,14]
# k=[7,16,11]

# for j in i[:]: 
#   for m in k[:]:
#     if (j%m==0):
#       j=j//2
#       m=m/2
#       print(j,m)
#     else:
#       j=j+m
#       m=m-j
#       print(j,m)

# class A:
#   def __init__(self,i=0):
#     self.i = i

# class B(A):
#   def __init__(self,j=2):
#     super().__init__()
#     self.j=j

# def main():
#   b= B(50)
#   print(b.i)
#   print(b.j)
# main()

# try:
#   fh = open("sasas","w")
#   fh.write("asdasd")
# else:
#   print("asdasd")
# except:
#   print(12412)
# finally:
#   print("asdasdasd")
#   fh.close()

# verification
# from itertools import combinations
# combs = combinations(arr,3)
# for c in combs:
#   print(c)


#%%
def findpeak_window(arr,w):
    """
    To find the preak from the array whose nearest w neighbors are
    smaller than it. We consider -inf valley on both sides of the array. 
    4 is peak for window = 2 if ==> 1 2 4 3 2, 2 1 4 2 3, 4 1 2, 3 2 4
    """
    if(len(arr) < w+1):
        raise IndexError(f"Array length is less than {w+1}")

    # let's check if edge elements are peak
    if arr[0]>max(arr[1 : (w+1)]) :
        return 0
    if arr[-1]>max(arr[-2:-(w+2):-1]):
        return len(arr)-1
    
    for i in range(w,len(arr)-w):
        if arr[i] > max( max(arr[ i-w : i ]), max(arr[i+1:i+w+1])):
            return i

    return('No Peak found!!')

# driver code:

arr1 = [1,2,3,1,4,5,5,4,5,3,1]
arr2 = [5,3,10]
arr3 = [1,2,3,1,4,5,8,4,5,3,1]
print(findpeak_window(arr1,1))
print(findpeak_window(arr2,2))
print(findpeak_window(arr3,3))
print(findpeak_window(arr3,4))
print(findpeak_window(arr3,5))
# %%
