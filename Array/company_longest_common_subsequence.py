def lcsLength(text1, text2) -> int:
  
  
  l1 = len(text1)
  if l1 == 0:
    return 0
  l2 = len(text2)
  
  i, j = 0, 0
  
  while j < l2:
    if text1[i] == text2[j]:
      i += 1
      j += 1
    else:
      j += 1
    if i == l1:
      break
      
  return i
  
text1 = "cat"
text2 = "crabt"
print(lcsLength(text1, text2))

text1 = "abcd"
text2 = "abcd"
print(lcsLength(text1, text2))

text1 = "abcd"
text2 = "efgh"
print(lcsLength(text1, text2))

text1 = "abcd"
text2 = ""
print(lcsLength(text1, text2))

text1 = ""
text2 = "abcd"
print(lcsLength(text1, text2))



