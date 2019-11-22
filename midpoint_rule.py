# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:10:51 2019

@author: Yuda Kurnia NF as @Kakatuahitam
"""
""" done at 11.31 """
# %%
from fractions import Fraction as F
def f(x):
    return 1/(1+x)


a,b = 1,0
n = 8

h = abs((b - a)/n)

p = [0,1,2,3,4,5,6,7]
r = [(i+1/2) for i in p]
xr = [(i)*h for i in r]
# %%
def find():
    """
    Formula:
        (h/2)(f0 + sigma(fi)n-1,  + fn)
                            i=1
        j = f0
        k = sigma(fi)n-1
                     i=1
        l = fn
        
    """
    print("*"*58)
    print((" Midpoint Integration Rule ".upper()).center(58,"*"))
    print("*"*58)
    
    print("*","Group 5:".ljust(54),"*")
    print("*","Yuda Kurnia NF".ljust(26), "|", "11180910000073".rjust(25),"*")
    print("*","Arjuna Putra Triansya".ljust(26), "|", "11180910000096".rjust(25),"*")
    print("*","Muhammad Haidar Fahmi".ljust(26), "|", "11180910000100".rjust(25),"*")
    print("*"*58, end="\n\n")
    
    # For return purpose
    x = []
    fx = []
    #
    
    k = 0
    for i in xr:
        x.append(i)
        fx.append(f(i))
        k += f(i)
        
    solution = h*k
    return solution, fx, x

# %%
x = []
fx = []
solution = 0

solution, fx, x = find()

print("Solution: ",solution)

print("="*58)
print("="," r ".center(17,"-"),"=", end="", sep="")
print(" xr ".center(17,"-"),"=", end="", sep="")
print(" f(xr) ".center(20,"-"),"=", sep="")

for i in range(len(x)):
    """print("\nr =", i)
    print("xr \t",x[i], sep="|")
    print("f(xr) \t",fx[i], sep="|")  
    print("_"*30)
    """
    print("=", str(F(r[i])).center(15), "=", str(x[i]).ljust(15), "=", str(fx[i]).ljust(18), "=")
    
print("="*58)
