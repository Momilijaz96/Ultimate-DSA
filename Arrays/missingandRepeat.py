import math
import numpy as np
import cmath
from decimal import Decimal

def missingAndRepeating(arr, n):
    arr = list(map(float,arr))
    orig_sum = float(sum(list(range(1,n+1))))
    arr_sum = float(sum(arr))
    #print(arr_sum,orig_sum)
    y = Decimal( arr_sum - orig_sum )
    x = Decimal(math.factorial(len(arr))) / Decimal(np.prod(arr))
    #print(math.factorial(len(arr)),np.prod(arr))
    r = y / (1-x)
    m = r*x
    m = int(np.round(float(m)))
    r = int(np.round(float(r)))
    return m,r