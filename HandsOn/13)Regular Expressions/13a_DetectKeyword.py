import re
s="Hi Anu! Good Afternooon"
pattern=input("Enter a pattern to search:")
if re.search(pattern.lower(),s.lower()):
    print("Keyword Found")
else:
    print("Keyword not found")
