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
min_coins_table = {1:1} #base case
def rec_change(target,coins):
    # min_coins = 1
    current_coin_counts = 0
    tgt = target
    for coin in coins[::-1]:
        if coin<=tgt:
            current_coin_counts += tgt//coin
            tgt = tgt - coin * (tgt//coin)

    return current_coin_counts

print(rec_change(10,[1,5,10]))
print(rec_change(8,[1,5,10]))
print(rec_change(13,[1,5,10]))
# %%
for x in range(21):
    print(x,rec_change(x,[1,5,10]))
# %%
min_coins_table = {1:1} #base case
def rec_change_dyn(target,coins):
    """
    Minimum coins needed to make change of target from coins.
    Assumption coins are sorted. if not use coins = sorted(coins) 
    """
    coins = sorted(coins,reverse=True)
    current_coin_counts = 0
    tgt = target
    for coin in coins:
        if coin<=tgt:
            current_coin_counts += tgt//coin
            tgt = tgt - coin * (tgt//coin)
            if min_coins_table.get(tgt,0):
                print("using memo")
                answer = current_coin_counts + min_coins_table.get(tgt)
                min_coins_table[target] = answer
                return answer
    min_coins_table[target] = current_coin_counts
    return current_coin_counts

print(rec_change_dyn(10,[1,5,10]))
print(rec_change_dyn(8,[1,5,10]))
print(rec_change_dyn(13,[1,5,10]))
print(rec_change_dyn(74,[1,5,10,25]))
for x in range(21):
    print(x,rec_change_dyn(x,[1,5,10]),end=' , ')
# %%