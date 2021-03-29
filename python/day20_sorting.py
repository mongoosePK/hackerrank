# day20_sorting.py
# william pulkownik
# write a bubble sort method and have it output the number of swaps and first, last elements

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bubbleSort(size, array):
    totalSwaps = 0
    for i in range(size):
        numSwaps = 0
        for j in range(size-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                numSwaps += 1
                totalSwaps += 1
        if numSwaps == 0:
            break
    
    print(f'Array is sorted in {totalSwaps} swaps.\nFirst Element: {array[0]}\nLast Element: {array[-1]}')

bubbleSort(n,a)