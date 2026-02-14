from shlex import join

sentence=input("Enter a sentence:")
abbreviations={"AI","ML","CNN","GNN"}
words=sentence.split()
ans=[]
for word in words:
    if word.upper() in abbreviations:
        ans.append(word.upper())
    else:
        ans.append(word.capitalize())
answer=" ".join(ans)
print(answer)