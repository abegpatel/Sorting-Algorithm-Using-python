# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:15:19 2021

@author: Abeg
"""
#insertation sort
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr
arr = [12, 11, 13, 5, 6] 
print(insertionSort(arr))
