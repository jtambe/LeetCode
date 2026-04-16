"""
Implement the OneEditApart function which checks if it's possible to get one string from another with no more than one correction (delete, add or change a symbol):

OneEditApart("cat", "dog") -> false 
OneEditApart("cat", "cats") -> true 
OneEditApart("cat", "cut") -> true 
OneEditApart("cat", "cast") -> true
OneEditApart("cat", "ct") -> true 
OneEditApart("cat", "at") -> true 
OneEditApart("cat", "acts") -> false
OneEditApart("cat", "catt") -> true
OneEditApart("cat", "cattt") -> false 
"""

def OneEditApart(str1: str, str2: str) -> bool:
    
    l1 = len(str1)
    l2 = len(str2)
    
    if abs(l1 - l2) > 1:
        return False
    
    i, j = 0, 0
    unmatched = 0
    
    while i < l1 and j < l2:
        if str1[i] != str2[j]:
            unmatched += 1
            if l1 < l2:
                j += 1
            elif l2 < l1:
                i += 1
            elif l1 == l2:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    
    return unmatched <= 1

print(OneEditApart("at", "cat"))# -> true 
print(OneEditApart("cat", "dog"))# -> false 
print(OneEditApart("cat", "cats"))# -> true 
print(OneEditApart("cat", "cut"))# -> true 
print(OneEditApart("cat", "cast"))# -> true
print(OneEditApart("cat", "ct")) #-> true  
print(OneEditApart("cat", "at"))# -> true 
print(OneEditApart("cat", "acts"))# -> false
print(OneEditApart("cat", "catt"))# -> true
print(OneEditApart("cat", "cattt"))# -> false 