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



# %%
def digits(number):
    # pythonic way
    number_str = str(number)
    digits_arr = list(map(int,number_str))
    return digits_arr

    #Standard way coming soon


# %%    
def multiply(arr,x):
    """
    To multiply the array arr as number with x and retutn array as answer.
    ex. [1,2,3]*5 = [6,1,5]
    """
    print(arr,x)
    multiplication_arr = []
    current_carry = 0
    for number in arr[::-1]: #array in reverse order
        multiplication = number*x + current_carry
        current_carry = (multiplication - multiplication%10)//10
        unit_digit = multiplication - (current_carry*10)
        multiplication_arr.insert(0,unit_digit)
        print(number,multiplication,unit_digit,current_carry)
        print(multiplication_arr)

    #to check if we have carry while multiplying last digit
    if current_carry:
        digits_in_current_carry = digits(current_carry)
        for digit in digits_in_current_carry[::-1]:
            multiplication_arr.insert(0,digit)
    return multiplication_arr
multiply([8, 7, 1, 7, 8, 2, 9, 1, 2, 0, 0], 15)

# %%
def big_factorial(n):
    """
    To find the factorial of a big number considering there is no bignum in the python using array.
    We take assumption that our factorial consumes more bits than available in the largest datatype available.
    """
    if n==0:
        return 1

    answer = [1]
    for x in range(2,n+1):
        answer = multiply(answer,x)
    
    return(answer)

big_factorial(15)

# %%
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
    
factorial(20)
# %%
