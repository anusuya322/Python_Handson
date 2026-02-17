def normalize_name(s):
    b=s.count(" ")
    if len(s)==0 or b==len(s):
        return ""
    else:
        s=s.strip()
        s=s.title()
        words=s.split()
        cleaned=" ".join(words)
        return cleaned
s=input()
ans=normalize_name(s)
print(ans)


