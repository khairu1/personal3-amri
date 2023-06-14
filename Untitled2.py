#!/usr/bin/env python
# coding: utf-8

# In[2]:


def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


# In[4]:


def recursionMethod(parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod(modified parameter)


# In[5]:


def firstMethod():
    secondMethod()
    print("l am the first method")
    
def secondMethod():
    thirdMethod()
    print("l am the second method")
    
def thirdMethod():
    fourthMethod()
    print("l am the third method")
    
def fourthMethod():
    print("l am the fourth method")


# In[6]:


def recursiveMethod(n):
    if n<1:
        print("n is less than l")
    else:
        recursiveMethod(n-1)
        print(n)


# In[7]:


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = power0fTwo(n-1)
        return power * 2


# In[8]:


def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


# In[9]:


def factorial(n):
    assert n>= 0 and int(n) == n, "The number must be positive integer only!"
    if n in [0,1]:
        return 1
    else:
        return n + factorial(n-1)


# In[11]:


def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   


# In[ ]:




