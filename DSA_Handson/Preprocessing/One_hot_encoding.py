from traceback import print_tb

cities=['Tokyo','Paris','NewYork']
#unique_cities=list(set(cities))
unique_cities=[]
for city in cities:
    if city not in unique_cities:
        unique_cities.append(city)
one_hot=[]
for city in cities:
    row=[]
    for uc in unique_cities:
        if uc==city:
            row.append(1)
        else:
            row.append(0)
    one_hot.append(row)
print("",unique_cities)
for ans in one_hot:
    print(ans)