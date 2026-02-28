import re
email="anusuyasm322@gmail.com"
domains=re.findall(r"@([A-Za-z0-9]+\.[A-Za-z]{2,}$)",email)
print(domains)
email_add="221001014@rajalakshmi.edu.in"
domain=email_add.split("@")[1]
print(domain)
res=re.findall(r"@([\w\.]+)",email_add)
print(res)