import csv

with open("st.csv", "r")as f:
    print(f.read())

# a=input("输入名称将会自动保存到name文件:")
# with open("a.txt","w") as f:
#     f.write(a)


lists = [["Top Gun", "RiskyBusiness", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
         ["Training Day", "Man on Fire", "Flight"]]
with open("al.csv", "w")as f:
    w = csv.writer(f, delimiter=",")
    for i in lists:
        w.writerow(i)
