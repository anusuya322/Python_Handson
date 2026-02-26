search=input("Enter a word:").lower()
count=0
with open("demo.txt","r") as f:
    for i in f:
        count+=i.lower().count(search)
    print(count)

