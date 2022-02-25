'''
from matplotlib import pyplot
import math
import numpy as np



inp1 = input("Enter the equation")
if (len(inp1) != 0):
    inp1 = inp1.split(' = ')
    print(inp1[1])
    if "^" in inp1[1]:
        var = inp1[1].split('^')
        print(var)
        if '+' in var[1]:
            num = var[1].split(" + ")
            print(var[0])
            print(num[0])
            print(num[1])
            ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
        
            if ("/" in num[0]):
                num1 = num[0].split("/")
                print(num1[0])
                print(num1[1])
               
                for i in range(21):
                    ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) + int(num[1])

                    
                pyplot.plot(ex1,ex2)
                
                pyplot.show()
            for i in range(21):
                ex2[i] = ex1[i]**int(num[0]) + int(num[1])

            
            pyplot.plot(ex1,ex2)
            pyplot.show()
        
        elif '-' in var[1]:
            num = var[1].split(" - ")
            print(var[0])
            print(num[0])
            print(num[1])

            ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            if ("/" in num[0]):
                num1 = num[0].split("/")
                print(num1[0])
                print(num1[1])
                
                for i in range(21):
                    ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) - int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            for i in range(21):
                ex2[i] = ex1[i]**int(num[0]) - int(num[1])
            pyplot.plot(ex1,ex2)
            pyplot.show()
        elif '*' in var[1]:
            num = var[1].split(" * ")
            print(var[0])
            print(num[0])
            print(num[1])

            ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            if ("/" in num[0]):
                num1 = num[0].split("/")
                print(num1[0])
                print(num1[1])
                
                for i in range(21):
                    ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) * int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            for i in range(21):
                ex2[i] = ex1[i]**int(num[0]) * int(num[1])
            pyplot.plot(ex1,ex2)
            pyplot.show()
        elif '/' in var[1]:
            num = var[1].split(" / ")
            print(var[0])
            print(num[0])
            print(num[1])

            ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            if ("/" in num[0]):
                num1 = num[0].split("/")
                print(num1[0])
                print(num1[1])
                for i in range(21):
                    ex2[i] = ex1[i]**(int(num1[0])/int(num1[1])) / int(num[1])
                pyplot.plot(ex1,ex2)
                pyplot.show()
            for i in range(21):
                ex2[i] = ex1[i]**int(num[0]) / int(num[1])
            pyplot.plot(ex1,ex2)
            pyplot.show()
        else:
            var = inp1[1].split('^')
            ex1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            ex2 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
            for i in range(21):
                ex2[i] = ex1[i]**int(var[1])
            pyplot.plot(ex1,ex2)
            pyplot.show()
'''
import math

def factorial(x):
    if(x==0 or x==1):
        x=1
    else:
        for i in range(1,x):
            x = x*(i)
    return x
def C(n,r):
    answer = factorial(n)/(factorial(n-r)*factorial(r))
    print(answer)
def P(n,r):
    answer = factorial(n)/factorial(n-r)
    print(answer) 
while True:
    no = input("Enter the number(n) :")
    n=int(no)
    ro = input("Enter the number(r) :")
    r=int(ro)
    C(n,r)
    P(n,r)


"""
x = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
y = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    y[i] =(x[i]*x[i]*x[i])

w = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
z = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    z[i] =(w[i]*w[i])

a = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
b = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    b[i] =(a[i]*a[i]*a[i]*a[i])

c = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
d = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    d[i] =c[i]

e = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
f = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    f[i] =math.sqrt(e[i])

g = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
h = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(11):
    h[i] =g[i]**(1/3)

pyplot.plot(x,y,label="third")
pyplot.plot(w,z,label="second")
pyplot.plot(a,b,label="fourth")
pyplot.plot(c,d,label="simple")
pyplot.plot(e,f,label="sqrt")
pyplot.plot(g,h,label="cbrt")

pyplot.legend(['third','second','fourth','simple','sqrt','cbrt'])
pyplot.show()
"""
