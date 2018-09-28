# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:09:11 2018

@author: Marzieh
"""

from __future__ import print_function
import torch
x=torch.empty(5,3)
print(x)

x1=torch.rand(5,3)
print(x1)

x2=torch.zeros(5,3,dtype=torch.long)
print(x2)

x3=torch.tensor([5.5,3])
print(x3)

x4=x.new_ones(5,3,dtype=torch.double)
print(x4)

x5=torch.randn_like(x, dtype=torch.float)
print(x5)

print(x.size())

y=torch.rand(5,3)
print(x+y)

print(torch.add(x,y))

#add x to y
y.add_(x)
print(y)