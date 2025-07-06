import functools
l1=[1,2,3,4]
def multi(a,b):
    return a*b
r=functools.reduce(multi, l1)
print(r)