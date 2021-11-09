def isdictkeyaalhpa(d):
    for k in d.keys():
        if not str(k).isalpha():
            return False
        return True
print(isdictkeyaalhpa({'a':2,'b':3}))
print(isdictkeyaalhpa({'a':2,'s':3}))

def PopByValue(_d,_v):
    result= []
    for k,v in _d.items():
        if v== _v:
            result.append((k,v))
    return result
print(PopByValue({'a':2,'b':3,'c':2},2))
