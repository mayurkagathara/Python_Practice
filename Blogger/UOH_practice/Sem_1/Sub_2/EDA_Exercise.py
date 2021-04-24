# %%
import numpy as np
from scipy.stats import median_abs_deviation,iqr
import math
np.random.seed(100)

# array = np.random.randint(0,1000,size=1000)
# array = [12,2,33,1,41,1,26,3,64,45,5,65,6,26,73]
array = [1,2,3,4,5,6,7,8,9,10]
print(f"{'Mean':>25}",np.mean(array))
print(f"{'Median':>25}",np.median(array))
print(f"{'Variance':>25}",np.var(array))
print(f"{'Standard Deviation':>25}", np.std(array))
quantiles = np.quantile(array,[0.25,0.50,0.75,0.90,0.99])
print(f"{'IQR':>25}",quantiles[2]-quantiles[0],iqr(array))
print(f"{'90perc':>25}",quantiles[3])
print(f"{'99perc':>25}",quantiles[4])
print(f"{'Median Absolute Deviation':>25}",median_abs_deviation(array))
'''
                     Mean 506.515
                   Median 503.0
                 Variance 86585.07377500001
       Standard Deviation 294.2534176097196
                      IQR 520.75
                   90perc 899.1
                   99perc 988.02
Median Absolute Deviation 383.2521
'''

# %%
def mean(arr):
    return sum(arr)/len(arr)
def median(arr):
    # check Smart way
    sorted_arr = sorted(arr)
    if len(arr)%2==1:
        return sorted_arr[math.ceil(len(sorted_arr)/2) - 1]
    else:
        left = (len(sorted_arr)//2) - 1
        right = (len(sorted_arr)//2)
        return mean([sorted_arr[left],sorted_arr[right]])
    
    # Smart way
    # return percentile(arr, 50)

def variance(arr):
    mean_value = mean(arr)
    variance_value = 0
    for ele in arr:
        variance_value += (ele-mean_value)**2
    return variance_value/len(arr)
def stdev(arr):
    return math.sqrt(variance(arr))
def percentile(arr, kth):
    if kth==0:
        return 0
    
    sorted_arr = sorted(arr)
    # linear interpolation
    left_ind = math.floor((len(arr)+1)*(kth/100)) - 1
    right_ind = math.ceil((len(arr)+1)*(kth/100)) - 1
    kth_precentile = mean([sorted_arr[left_ind],sorted_arr[right_ind]])
    return kth_precentile


def IQR(arr):
    return percentile(arr,75) - percentile(arr,25)
def MAD(arr):
    median_value = median(arr)
    MADiv = [abs(ele - median_value) for ele in arr]
    return median(MADiv)

# %%
print('-'*50)
print(f"{'Mean':>15}",mean(array))
print(f"{'Median':>15}",median(array))
print(f"{'Variance':>15}",variance(array))
print(f"{'Standard Deviation':>15}", stdev(array))
print(f"{'IQR':>15}",IQR(array))
print(f"{'90perc':>15}",percentile(array,90))
print(f"{'99perc':>15}",percentile(array,99))
print(f"{'MAD':>15}",MAD(array))
# %%
