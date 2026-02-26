import pickle

li=[{"Book":"Ikigai","Year":2015,"Author":"Jp"},
    {"Book":"Compound Effect","Year":2022,"Author":"Darren Hardy"},
    {"Book":"Unfinished","Year":2020,"Author":"Priyanka Chopra"}
    ]
with open("book.csv","wb") as f:
    pickle.dump(li,f)
with open("book.csv","rb") as f:
    data=pickle.load(f)
print(data)
