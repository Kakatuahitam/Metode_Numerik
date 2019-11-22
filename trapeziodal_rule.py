# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:09:16 2019

@author: Yuda Kurnia NF as @Kakatuahitam
"""
""" done at 10.54 """
# %%
def f(x):
    return 1/(1+x)

a,b = 1,0
n = 8

h = abs((b - a)/n)

r = [i for i in range(n+1)]
xr = [abs(i*h) for i in r]
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
    print("*"*48)
    print((" Trapezoidal Integration Rule ".upper()).center(48,"*"))
    print("*"*48)
    
    print("*","Group 5:".ljust(44),"*")
    print("*","Yuda Kurnia NF".ljust(21), "|", "11180910000073".rjust(20),"*")
    print("*","Arjuna Putra Triansya".ljust(21), "|", "11180910000096".rjust(20),"*")
    print("*","Muhammad Haidar Fahmi".ljust(21), "|", "11180910000100".rjust(20),"*")
    print("*"*48, end="\n\n")
    
    # For return purpose
    x = []
    fx = []
    #
    
    k = 0
    for i in xr:
        x.append(i)
        fx.append(f(i))
        
        if i != xr[0] and i != xr[-1]:
            k += f(i)   
        
    j = f(xr[0])
    l = f(xr[n])
    
    solution = (h/2)*(j+2*k+l)
    return solution, fx, x

# %%
x = []
fx = []
solution = 0

solution, fx, x = find()

print("Solution: ",solution)

print("="*48)
print("="," r ".center(7,"-"),"=", end="", sep="")
print(" xr ".center(17,"-"),"=", end="", sep="")
print(" f(xr) ".center(20,"-"),"=", sep="")

for i in range(len(x)):
    """print("\nr =", i)
    print("xr \t",x[i], sep="|")
    print("f(xr) \t",fx[i], sep="|")  
    print("_"*30)
    """
    print("=", str(i).center(5), "=", str(x[i]).ljust(15), "=", str(fx[i]).ljust(18), "=")
    
print("="*48)
