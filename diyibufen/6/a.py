a = "Camus"
for i in range(5):
    print(a[i])

# a=input("Enter a")
# # b=input('Enter b')
# #
# # c="Yesterday I wrote {}.".format(a)
# # print(c)
# # print("Isent it to {}!".format(b))


a = "aldous Huxley was born in 1894".capitalize()
print(a)

a = "Where now?. Who now?. When now?".split(".")
print(a)

a = ["The", "fox", "jumped", "over", "the", "fence", "."]
a = " ".join(a)
a = a[0:-2] + a[-1]
print(a)

a = "A screaming comes across the sky.".replace("s", "$")
print(a)

print("Hemingway".index("m"))

print('"在你最喜欢的书中找一段对话，将其变成一个字符串"')

print("three " * 3)

a = "It was bright cold day in April, and the clocks were striking thirteen,"
i = a.index(",")
print(a[:i])
