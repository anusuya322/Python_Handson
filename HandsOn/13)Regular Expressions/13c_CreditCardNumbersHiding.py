import re
credit_num=input("Enter your credit card number:")
'''li2=[]
for i in range(len(credit_num)-4):
    li2.append("*")
for j in range(12,len(credit_num)):
    li2.append(credit_num[j])
print(li2)
st=""
for i in range(len(credit_num)):
    st+=li2[i]
print(st)'''
encrypt=re.sub(r"\d{12}(\d{4})",r"************\1",credit_num)
print(encrypt)