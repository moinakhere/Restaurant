import mysql.connector
from colorama import Fore
import pickle
import datetime


s=[]
with open("password.dat", "rb") as f:
    try:
        while True:
            s = pickle.load(f)
    except EOFError:
        pass

conn = mysql.connector.connect(host= str(s[0]), user= str(s[1]), password= str(s[2]), database= str(s[3]))
cur = conn.cursor()
cur.execute("select * from item")
r = cur.fetchall()
item = []
for i in r:
    item.append([i[0], i[1], i[2], i[3]])

item_list={}

def sorting(cost):
    print(
        "1. Starters\n2. Soup\n3. Salad\n4. Vegetarian Main Course\n5. Non-Vegetarian Main Course\n6. Naan\n7. Paratha\n8. Kulcha\n9. Roti\n10. Dal\n11. Sides\n12. Beverages\n13. Desserts\n14. Chef special\n15. All"
    )
    d = {
        1: "Starters",
        2: "Soup",
        3: "Salad",
        4: "Vegetarian Main Course",
        5: "Non-Vegetarian Main Course",
        6: "Naan",
        7: "Paratha",
        8: "Kulcha",
        9: "Roti",
        10: "Dal",
        11: "Sides",
        12: "Beverages",
        13: "Desserts",
        14: "Chef special",
        15: "",
    }
    serial = int(input("Enter the number of the type of item you want:"))
    for dic_item in d.keys():
        if serial == dic_item:
            cur.execute("select * from item where type like '{}%'".format(d[serial]))
            rec = cur.fetchall()
            print(
                "%15s" % (Fore.MAGENTA + "No"),
                "%34s" % (Fore.BLUE + "Name"),
                "%35s" % (Fore.LIGHTGREEN_EX + "Type"),
                "%20s" % (Fore.LIGHTYELLOW_EX + "Price"),
            )
            print(Fore.LIGHTCYAN_EX + ("*" * 120))
            for j in rec:
                print(
                    "%15s" % (Fore.MAGENTA + (str(j[0]))),
                    "%34s" % (Fore.BLUE + (str(j[1]))),
                    "%35s" % (Fore.LIGHTGREEN_EX + (str(j[2]))),
                    "%20s" % (Fore.LIGHTYELLOW_EX + (str(j[3]))),
                )
            print(Fore.RESET)
            z= order(cost)
        elif serial > 15 or serial < 1:
            print("Sorry! no such item found")
            break
    return z


def order(cost):
    a = int(input("Enter the item's number you want\n"))
    for it in item:
        if int(a) == it[0]:
            z = int(input("How many do you want?\n"))
            cost += int(it[3]) * z
            item_list[i[1]] = [it[3], z]
    return cost


while True:
    c=sorting(0)
    if input("Do you want to order more items?\n").lower() in "yes":
        continue
    else:
        break
print(Fore.LIGHTCYAN_EX + ("*" * 120))
sc=1
for i in item_list.keys():
    print(
        "%5s"% (Fore.GREEN + str(sc)),
        "%25s" % (Fore.MAGENTA + (str(i))),
        "%34s" % (Fore.BLUE + (str(item_list[i][0]))),
        "%35s" % (Fore.LIGHTGREEN_EX + (str(item_list[i][1]))),
    )
    sc+=1
print(Fore.LIGHTYELLOW_EX + str("Total total_cost: ₹" + "%70s" % str(c)))
print(Fore.LIGHTGREEN_EX + ("=" * 120))
print(Fore.LIGHTMAGENTA_EX + str("Final cost(with 18 percent GST): ₹" + "%50s" % str(c * 1.18)))
print(Fore.RESET)
cur.execute(
    "insert into sell values('{}', '{}', '{}')".format(
        datetime.datetime.now().strftime("%Y-%m-%d"),
        datetime.datetime.now().strftime("%H:%M:%S"),
        str(c)
    )
)
conn.commit()
conn.close()
