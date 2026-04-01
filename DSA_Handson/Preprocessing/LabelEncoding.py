data=['Male','Female','Male','Female']
map={}
encoded=[]
count=0
for i in data:
    if i not in map:
        map[i]=count
        count+=1
    encoded.append(map[i])
print(map)
print(encoded)