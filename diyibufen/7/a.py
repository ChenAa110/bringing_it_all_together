a = ["The Walking Dead", "Entourage", "The Sopranos", "The VampireDiaries"]

for i in a:
    print(i)

for i in range(25, 51):
    print(i)

for i in a:
    print(i, a.index(i))

for index, show in enumerate(a):
    print(index, show)

number = [1, 4, 65]

while True:
    print("enter q is exit!")
    q = input("猜数字")
    if q == "q":
        break
    try:
        q = int(q)
    except ValueError:
        print("please type a number or q to quit.")
    if q in number:
        print("you win")
    else:
        print("you lost")

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
add = []
for i in list1:
    for j in list2:
        add.append(i * j)

print(add)