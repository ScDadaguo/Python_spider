def panduan(s):
    if ('@' in s) and (s.index('@')!=0)and (s.index('@')!=len(s)-1):
        return True
    else: return  False
b={1:"232",2:"ss@ss",3:"wsss",4:"sss",55:"ssddf"}
l=(list)(b.values())
for i in l :
    if panduan(i):
        print(i)



