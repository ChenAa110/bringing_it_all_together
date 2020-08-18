a = "Hello".upper()
b = "Hello".replace("o", "@")
print(a, b)

# list
fruit = ['apple', 'orange', 'pear']
fruit.append("banana")
fruit.append("peach")
fruit.append(True)
fruit.append(123)
fruit.append(1.1)
print(fruit)
print(fruit[1])
fruit[7] = 1.01
print(fruit)
fruit.pop()
print(fruit)
# print(fruit[10])

a = "apple" in fruit
print(a)
b = '101' not in fruit
print(b)
print(len(fruit))

colors = ['purple', 'orange', 'green']
guess = input("Guess a color:")

if guess in colors:
    print("you guessed correctly!")
else:
    print("Wrong try again")

# tuple
rndm = ("M,jackson", 1985, True)

print(rndm)
print(rndm[1])
print(a in rndm)
print(a not in rndm)

# dict
fruits = {"apple": "red", "banana": "yellow"}
print(fruits)

facts = dict()
facts["code"] = "fun"
print(facts["code"])

facts["Bill"] = "Gates"
print(facts["Bill"])

facts["founded"] = 1776
print(facts["founded"])

bill = dict({"Bill Gates": "charitable"})
print("Bill Gates" in bill)
print("Bill Gates" not in bill)

books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}

del books["The Trial"]
print(books)

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }
n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("not found")

lists = []
rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]
rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]
djs = ["Zeds Dead", "Titsto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)

locations = []
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)
print(locations)

eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ny = {"locations": (41.8781, 87.6298), "celebs": ["W.Allen", "Jay Z", "K.Bacon"],
      "facts": {"state": "NY", "country": "America"}}

print(ny)