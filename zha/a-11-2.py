import re
import math

p = r'\w+@qq\.com'
text = "tone emaill is 124@qq.com "
text1 = "tone emaill is 124@qq1.com "
emaill = '12@qq.com'
emaill1 = '12@qq1.com'
pj = r'java|Java|JAVA'
tpj = 'you like java and JAVA nnd Java'

m = re.match(p, emaill)
print(type(m))
print(m)

m1 = re.match(p, emaill1)
print(m1)

m = re.search(p, text)
print(m)
m = re.search(p, text1)
print(m)

m = re.findall(pj, tpj)
print(m)

p = r'\d+'
text = 'ABCDE12F3g'
repace_text = re.sub(p, '  ', text)
print(repace_text)
repace_text = re.sub(p, '  ', text,count=1)
print(repace_text)
repace_text = re.sub(p, '  ', text,count=2)
print(repace_text)


p = r'\d+'
text = 'ABCDE12F3g'
clist=re.split(p,text)
print(clist)
clist=re.split(p,text,maxsplit=1)
print(clist)
clist=re.split(p,text,maxsplit=2)
print(clist)


print(math.floor(-1.6))
print(math.ceil(-1.6))



