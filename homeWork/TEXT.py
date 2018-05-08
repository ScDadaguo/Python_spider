a=[2,3,-3,-5,-3,-5,4,2,5,2]
b=a.copy()
for i in a:
    if i<0:
        b.remove(i)
print(b)


