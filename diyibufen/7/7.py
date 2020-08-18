name = "Ted"
for character in name:
    print(character)

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

shows = ("a GOT", "Narcos", "Vice  sa")
for show in shows:
    print(show)

shows = {"a GOT1": "ac", "Narcos1": "ab", "Vice  sa1": "ad"}
for show in shows:
    print(show)

t = ["ac", "ab", "ad"]
i = 0
for show in t:
    new = t[i]
    new = new.upper()
    t[i] = new
    i += 1

print(t)
t = ["ac", "ab", "ad"]
for i, show in enumerate(t):
    new = t[i]
    new = new.upper()
    t[i] = new
print(t)

t1 = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Dev", "friends", "Always Sunny"]
all_show = []

for show in t1:
    show = show.upper()
    all_show.append(show)
for show in coms:
    show = show.upper()
    all_show.append(show)
print(all_show)

x = 10
while x > 0:
    print("{}".format(x))
    x -= 1
print("Happy new year")

t1 = ["what is your name", "what is your fav,color", "what is your quest"]
n = 0
while True:
    print("tyep q to quit")
    a = input(t1[n])
    if a == 'q':
        break
    n = (n + 1) % 3

for i in range(1, 3):
    print(i)
    for letter in ["a", 'b', 'c']:
        print(letter)

list1 = [1, 3, 5]
list2 = [2, 4, 6]
add = []
for i in list1:
    for j in list2:
        add.append(i + j)

print(add)


while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)
