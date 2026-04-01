with open("log.txt","r") as f:
    data=f.read()
    li=data.split("\n")
    print(li)
    freq={}
    #keys=["INFO","WARN","ERROR"]
    for l in li:
        if l.strip()=="":
            continue
        event=l.split()[0]
        freq[event]=freq.get(event,0)+1
    print(freq)
    max_count=0
    for key,count in freq.items():
        if count>max_count:
            max_count=count
            ans=key
    print(ans)

