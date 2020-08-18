author = 'Kafka'

for i in range(5):
    print(author[i])

print(author[1])

f = 'a'
f = 'b'
print(f)

a = "cat" * 3
print(a)

print(a.upper())
print(a.lower())
print(a.capitalize())
print("cat {}".format("a"))
print("cat {}".format(a))

print("{}cat {}".format(a, f))

# n = input("Enter a noun:")
# v = input("Enter a verb:")
# adj = input("Enter a adj")
# n2 = input("Enter a noun:")
#
# r = """The {} {} the {} {}
#     """.format(n,v,adj,n2)
# print(r)

a = "ccccc.bbbb.dddd!".split(".")
print(a)

a = "abc"
result = "+".join(a)
print(result)

a = " a b c "
print(a)
print(a.strip())

a = "aaccaa"
print(a.replace("aa", "dd"))

print(a.index("c"))

print("c" in a)

print("b" not in a)

print("aaa\"c\"")

fict = ["Tolstoy", "Camus", "Huxley", "Austin"]
print(fict[0:3])

ivan="""in place of death there was light。"""

print(ivan[0:17])
print(ivan[17:33])

