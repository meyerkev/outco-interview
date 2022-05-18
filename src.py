#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumStepsToOne' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER num as parameter.
#
import heapq

def minimumStepsToOne(num : int):
    if num == 1:
        return 0
    cache = { 1:0 }
    queue = [1]
    while queue:
        invariant_num = heapq.heappop(queue)
        if invariant_num > num:
            continue
        cache_steps = cache[invariant_num]
        def keep_going(n):
            if n > num:
                return
            if not n in cache or cache[n] > cache_steps + 1:
                cache[n] = cache_steps + 1
                heapq.heappush(queue, n)

        keep_going(invariant_num * 3)
        keep_going(invariant_num * 2)
        keep_going(invariant_num + 1)

    return cache[num]

if __name__ == '__main__':
    num = int(input().strip())
    result = minimumStepsToOne(num)
    print(result)
