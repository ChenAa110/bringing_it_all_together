s_dict = {102: '张三', 105: '李四', 109: '王五'}

print('----遍历健-----')

for s_id in s_dict.keys():
    print(s_id)

print('----遍历值-----')
for s_value in s_dict.values():
    print(s_value)

print('----遍历健:值-----')
for s_id, s_value in s_dict.items():
    print('{}:{}'.format(s_id, s_value))

wordstring = """
    it was the  best of times it was the worst of times.
    it was the age if wusdom it was age of foolishness.
"""

wordstring = wordstring.replace(".", '')
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

d = dict(zip(wordlist, wordfreq))
print(d)

s = "World"

print(s[-1::-1])


def calc(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    else:
        return lambda a, b: (a - b)


f1 = calc('+')
f2 = calc('-')
print("10 + 5={0}".format(f1(10, 5)))
print('10-5={0}'.format(f2(10, 5)))



data1=[66,15,91,28,98,60,7,89,99]

filtered=filter(lambda x:(x>50),data1)
data2=list(filtered)
print(data2)

mapped=map(lambda x:(x*2),data1)
data3=list(mapped)
print(data3)



