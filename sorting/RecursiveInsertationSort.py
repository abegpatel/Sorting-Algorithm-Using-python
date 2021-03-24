# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:16:17 2021

@author: Abeg
"""
#recursive insertationSort
def insertationsort(arr):
  isort(arr,len(arr))
  return arr
def isort(arr,k):
  if k>1:
    isort(arr,k-1)
    insert(arr,k-1)
def insert(arr,k):
  pos=k
  while pos >0 and arr[pos]<arr[pos-1]:
    arr[pos],arr[pos-1]=arr[pos-1],arr[pos]
    pos=pos-1
print(insertationsort([1,4,3,2,5,6,9,8]))
