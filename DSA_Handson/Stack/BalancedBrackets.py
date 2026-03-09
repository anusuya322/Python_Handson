def isvalid(s):
 stack=[]
 di={'}':'{',']':'[',')':'('}
 for ch in s:
  if ch in '({[':
    stack.append(ch)
  else:
    if not stack or stack[-1]!=di[ch]:
        return False
    stack.pop()
 if len(stack)==0:
    return True
 return False
s=input()
ans=isvalid(s)
print(ans)