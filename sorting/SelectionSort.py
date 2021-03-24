# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:14:27 2021

@author: Abeg
"""
#selection sort
def selectionsort(arr):
  for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
      if(arr[min]>arr[j]):
        min=j
    arr[i],arr[min]=arr[min],arr[i]
  return arr
arr=[2,4,9,6,3,1,8]
print(selectionsort(arr))
