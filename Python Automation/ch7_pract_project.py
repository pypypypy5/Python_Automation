import re

def striiip(stri, ridof):
    if ridof:
        regex = re.compile(ridof)
        mo = regex.sub('',stri)
        return mo
    else:
        return stri[1:-1]
    
st = input()
getridof = input()
print(striiip(st,getridof))