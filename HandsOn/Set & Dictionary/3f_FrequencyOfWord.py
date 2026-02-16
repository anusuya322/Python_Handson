para=input("Enter the sentence:")
words=para.split()
freq_d={}
for word in words:
    if word in freq_d:
        freq_d[word]+=1
    else:
        freq_d[word]=1
print(freq_d)
sort_dict=dict(sorted(freq_d.items(),key=lambda x:x[1]))
print(sort_dict)
'''d1={}
for word in words:
    d1[word]=d1.get(word,0)+1
print(d1)'''