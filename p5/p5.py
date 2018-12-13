# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:15:28 2018

@author: furqa
"""

for n in range(2,30):
    s=n-1
    found =False
    while not found:
        s+=1
        found = False
        for i in range(n,1,-1):
            if s%i != 0:
                found =False                
                break
            else:            
                found=True
                
    print("found",s,"for",n)    