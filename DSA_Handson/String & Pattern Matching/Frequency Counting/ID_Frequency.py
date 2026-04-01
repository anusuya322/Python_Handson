li_id=[100,240,248,100,300,240,560]
freq={}
for id in li_id:
    freq[id]=freq.get(id,0)+1
print(freq)
ans=[]
for id,count in freq.items():
    if count>1:
        ans.append(id)
print("Id appearing more than once",ans)
