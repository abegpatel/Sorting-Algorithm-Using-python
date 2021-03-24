# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:17:27 2021

@author: Abeg
"""

#merge sort
def merge(A,B):
  (L,m,n)=([],len(A),len(B))
  (i,j)=(0,0)
  while i+j<m+n:
    if i==m:
      L.append(B[j])
      j=j+1
    elif j==n:
      L.append(A[i])
      i=i+1
    elif A[i]<=B[j]:
      L.append(A[i])
      i=i+1
    elif A[i]>B[j]:
      L.append(B[j])
      j=j+1
  return L
def mergesort(arr,l,r):
  if r-l<=1:
    return arr[l:r]
  if r-l>1:
    m = (l+(r-1))//2
    L=mergesort(arr, l, m) 
    R=mergesort(arr, m+1, r) 
    return merge(L,R) 
  
  
arr=[2,5,8,9,3,5,7]
n=len(arr)
mergesort(arr,0,n)
print(arr)