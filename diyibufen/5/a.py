lists = []
a = ["Kanye West", "Jay Z", "Eminem", "Nas"]
lists.append(a)
print(lists)

locations = [(34.0522, 188.2437), (41.8781, 87.6298)]

my = {"height": "171", "width": "70", "color": "yellow"}

answer = input("Type height, fav_color or fav_author")
if answer in my:
    result = my[answer]
    print(result)


songs = {"John Lennon": "Stand by Me",
         "Kanye West": "Homecoming",
         "Swedish House Mafia": "Don't You Worry Child"
}