import datetime


d=datetime.datetime(2020,1,29,23,59,59,100000)
print(d)

d=datetime.datetime.today()
print(d)

d=datetime.datetime.now(tz=None)
d1=datetime.datetime.now()
print(d)
print(d1)

# d=datetime.fromtimestamp（timestamp，tz=None）
d=datetime.datetime.fromtimestamp(999,tz=None)
print(d)

d=datetime.date.today()
print(d)
otherstyletime=d.strftime("%Y%m%d")
print(otherstyletime)

d=datetime.date(2021,2,28)
print(d)
otherstyletime=d.strftime("%Y%m%d")
print(otherstyletime)

d=datetime.date.today()
print(d.strftime("%Y%m%d"))



d=datetime.date.fromtimestamp(999)
print(d)

d=datetime.time()
print(d)

d=datetime.date.today()
delta=datetime.timedelta(10)
d+=delta
print(d)

d=datetime.date.today()
delta=datetime.timedelta(-10)
d+=delta
print(d)

d=datetime.date.today()
delta=datetime.timedelta(weeks=5)
d+=delta
print(d)


d=datetime.date.today()
delta=datetime.timedelta(weeks=-5)
d+=delta
print(d)