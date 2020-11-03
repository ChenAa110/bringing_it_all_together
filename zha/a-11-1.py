import datetime

strd = '2020/09/02'
d = datetime.datetime.strptime(strd, '%Y/%m/%d')
print(d)

print(type(strd))