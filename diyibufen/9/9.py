import csv

st = open("my_file.txt", "w")
st.write("Hi from Python!")
st.close()

with open("st.txt", "w") as f:
    f.write("hi from this one")

my_list = []
with open("my_file.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
print(my_list)

with open("st.csv", "w")as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three k"])
    w.writerow(["four", "five", "six"])

with open("st.csv", "r")as f:
    print(f.read())

with open("st.csv", "r")as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
