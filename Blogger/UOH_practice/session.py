#%%
n = 10
# ans = 8
# sl_digit = 0
# l_digit = 1

# for i in range(1,n+1):
#     current_fibo = sl_digit+l_digit
#     sl_digit = l_digit
#     l_digit = current_fibo
#     print(current_fibo)

# Recursive method of O(n^2)
def ways(steps):
    print("steps ",steps)
    if steps==1:
        return 1
    if steps==2:
        return 2
    return ways(steps-1) + ways(steps-2)
# driver code
ways(10)



# DP method with O(n)
# %%
answers_dict = {1:1,2:2}
def ways_dyn(steps):
    print(steps)
    if steps==1:
        return 1
    if steps==2:
        return 2
    # print(answers_dict)

    if answers_dict.get(steps-1, 0) > 0:
        l_number = answers_dict.get(steps-1, 0)
    else:
        l_number = ways_dyn(steps-1)

    if answers_dict.get(steps-2, 0) > 0:
        sl_number = answers_dict.get(steps-2, 0)
    else:
        sl_number = ways_dyn(steps-2)
    
    ans = l_number+sl_number
    # print("ans",ans)
    answers_dict[steps] = ans

    return ans

print(ways_dyn(10))
print(answers_dict)


# %%
