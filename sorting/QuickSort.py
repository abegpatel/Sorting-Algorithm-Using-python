# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:18:23 2021

@author: Abeg
"""

#quick sort
def partitation(arr,low,high):
  i=low-1
  pivot=arr[high]
  if high-low<=1:
    return 0
  for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  arr[i+1],arr[high] = arr[high],arr[i+1] 
  return ( i+1 ) 
def quicksort(arr,low,high):
  if low<high:
    pi=partitation(arr,low,high)
    quicksort(arr, low, pi-1) 
    quicksort(arr, pi+1, high) 
arr=[1,3,8,7,9,2]
n=len(arr)
print(quicksort(arr,0,n-1))
print(arr)
