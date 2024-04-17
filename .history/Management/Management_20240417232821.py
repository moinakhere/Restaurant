"""
This module provides random number generators for various distributions.

The basic interface is simple: you create a random number generator object,
and then use one of the methods on the object to generate random numbers.

The random module is implemented in C and has no explicit dependency on the
interpreter or the rest of the Python Standard Library.
"""
import random
import datetime
import pickle
import mysql.connector
from colorama import Fore

s = []
with open("password.dat", "rb") as f:
    try:
        while True:
            s=pickle.load(f)
    except EOFError:
        pass


acs = []


# DELETING
def wrkdlt():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    cur.execute(
        "delete from workers where code='{}'".format(input("Enter worker code:"))
    )
    conn.commit()
    print("Employee's detail has been deleted.")
    conn.close()


def stkdlt():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    g = input("Enter stock id:")
    cur = conn.cursor()
    cur.execute("delete from stock where id='{}'".format(g))
    conn.commit()
    conn.close()


# ADDING
def wrkadd():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    curx = conn.cursor()
    ans = "y"
    while ans.lower() in "yes":
        nm = input("Enter worker name:").title()
        jb = input("Enter job:").title()
        sal = int(input("Enter salary:"))
        curx.execute("select * from workers")
        r = curx.fetchall()
        it = []
        for i in r:
            it.append(i[0])
        x = True
        while x is True:
            t = chr(random.randrange(65, 91)) + chr(random.randrange(97, 123))
            if t not in it:
                cur.execute(
                    "insert into workers values('{}','{}','{}','{}')".format(
                        t, nm, jb, sal
                    )
                )
                conn.commit()
                it.append(t)
                x = False
                print("Your id is", t)
            else:
                x = True
        ans = input("Are there more new joines?:")
    conn.close()
    print("Data of all the new joines have been added")


def itadd():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    ans = "y"
    while ans.lower() in "yes":
        iname = input("Enter item name:").title()
        pr = float(input("Enter price:"))
        print(
            "1. Starters\n2. Soup\n3. Salad\n4. Vegetarian Main Course\n5. Non-Vegetarian Main Course\n6. Naan\n7. Paratha\n8. Kulcha\n9. Roti\n10. Dal\n11. Sides\n12. Beverages\n13. Desserts\n14. Chef special\n15. All"
        )
        ty = input("Enter cuisine type from the above list if present:")
        z = "insert into Item values('{}','{}','{}','{}')".format(0, iname, ty, pr)
        cur.execute(z)
        conn.commit()
        ans = input("Do you want to add more item?:")
    conn.close()
    print("All items have been added to the menu.")


def stkadd():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    curx = conn.cursor()
    ans = "y"
    while ans.lower() in "yes":
        d = input("Stock name:")
        n = float(input("Unit rate of stock:"))
        m = int(input("Units of stock bought:"))
        curx.execute("select * from stock")
        r = curx.fetchall()
        it = []
        for i in r:
            it.append(i[0])
        x = True
        while x is True:
            g = chr(random.randrange(65, 91)) + str(random.randrange(10))
            if g not in it:
                cur.execute(
                    "insert into stock values ('{}','{}','{}','{}')".format(g, d, n, m)
                )
                conn.commit()
                it.append(g)
                x = False
                print("Item id of", d, "is", g)
            else:
                x = True
        ans = input("Do you want to add more items?\n")
    conn.close()


# DISPLAYING
def selldisp():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur=conn.cursor()
    print("1. Today's sell\n2. Last month's sell\n3. Total Sell\n")
    z=input("Enter choice:").lower()
    if z=="1":
        cur.execute("select * from sell where date='{}'".format(datetime.datetime.now().strftime("%Y-%m-%d")))
        r=cur.fetchall()
        print(
            "%45s" % (Fore.YELLOW + ("Date")),
            "%45s" % (Fore.CYAN + ("Time")),
            "%15s" % (Fore.RED + ("Sell"))
        )
        print("*"*120)
        for i in r:
            print(
                "%45s" % (Fore.CYAN + str(i[0])),
                "%45s" % (Fore.RED + str(i[1])),
                "%15s" % (Fore.GREEN + (str(i[2]))),
            )
        print("*"*120)    
        cur.execute(
            "select sum(Sell) from sell where date='{}'".format(
                datetime.datetime.now().strftime("%Y-%m-%d")
            )
        )
        sell_today = cur.fetchall()
        print("Today's total sale:",sell_today[0][0])
        '''cur.execute(
            "select sum(Sell) from sell where date='{}'".format(
                datetime.date.today() - datetime.timedelta(days=1)
            )
        )
        sell_yesterday = cur.fetchall()
        sell_diff= sell_today - sell_yesterday
        if sell_diff>0:
            print("There is a profit of",((sell_diff/sell_yesterday)*100))'''
    elif z==2:
        cur.execute("SELECT * FROM sell WHERE MONTH(date) = '{}'".format((datetime.datetime.now().month)-1))
        r = cur.fetchall()
        if len(r)>0:
            print(
                "%45s" % (Fore.YELLOW + ("Date")),
                "%45s" % (Fore.CYAN + ("Time")),
                "%15s" % (Fore.RED + ("Sell"))
                )
            print("*" * 120)
            for i in r:
                print("%45s" % (Fore.CYAN + str(i[0])),
                      "%45s" % (Fore.RED + str(i[1])),
                      "%15s" % (Fore.GREEN + (str(i[2])))
                      )
            print("*" * 120)
            cur.execute("select sum(sell) where month(date)='{}'".format((datetime.datetime.now().month)-1))
            r = cur.fetchall()
            if len(r)>=1:
                print("This month's total sale:", r[0])
        else:
            print("No sell today.")
    elif z==3:
        cur.execute("select * from sell")
        r = cur.fetchall()
        print(
            "%45s" % (Fore.YELLOW + ("Date")),
            "%45s" % (Fore.CYAN + ("Time")),
            "%15s" % (Fore.RED + ("Sell"))
        )
        print("*" * 120)

    print(Fore.RESET)
    conn.close()


def wrkdisp():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    cur.execute("select * from workers")
    r = cur.fetchall()
    print(
        "%5s" % (Fore.YELLOW + ("Code")),
        "%23s" % (Fore.CYAN + ("Name")),
        "%35s" % (Fore.RED + "Job"),
        "%34s" % (Fore.GREEN + "Sal"),
    )
    print("*" * 120)
    for i in r:
        print(
            "%5s" % (Fore.YELLOW + str(i[0])),
            "%25s" % (Fore.CYAN + str(i[1])),
            "%35s" % (Fore.RED + str(i[2])),
            "%35s" % (Fore.GREEN + (str(i[3]))),
        )
    print(Fore.RESET)
    conn.close()


def stdisp():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    wrk_d = input("Enter your ID:")
    cur = conn.cursor()
    cur.execute("select * from workers where code='{}'".format(wrk_d))
    r = cur.fetchall()
    d=[]
    for i in range(4):
        d.append(r[0][i])
    print(
        "%5s" % (Fore.YELLOW + ("Code")),
        "%23s" % (Fore.CYAN + ("Name")),
        "%35s" % (Fore.RED + "Job"),
        "%34s" % (Fore.GREEN + "Sal"),
    )
    print("*" * 120)
    print(
        "%5s" % (Fore.YELLOW + str(d[0])),
        "%25s" % (Fore.CYAN + str(d[1])),
        "%35s" % (Fore.RED + str(d[2])),
        "%35s" % (Fore.GREEN + (str(d[3]))),
    )
    print(Fore.RESET)
    conn.close()


def stkdisp():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    cur.execute("select * from stock")
    r = cur.fetchall()
    print(
        "%5s" % (Fore.YELLOW + ("Id")),
        "%23s" % (Fore.CYAN + ("Name")),
        "%22s" % (Fore.RED + "Unit Price"),
        "%16s" % (Fore.GREEN + "Unit"),
    )
    print("*" * 60)
    for i in r:
        print(
            "%5s" % (Fore.YELLOW + str(i[0])),
            "%25s" % (Fore.CYAN + str(i[1])),
            "%20s" % (Fore.RED + str(i[2])),
            "%15s" % (Fore.GREEN + (str(i[3]))),
        )
    print(Fore.RESET)
    conn.close()


def itdisp():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    cur.execute("select * from item")
    r = cur.fetchall()
    print(
        "%15s" % (Fore.MAGENTA + "No"),
        "%34s" % (Fore.BLUE + "Name"),
        "%35s" % (Fore.LIGHTGREEN_EX + "Type"),
        "%20s" % (Fore.LIGHTYELLOW_EX + "Price"),
    )
    print(Fore.LIGHTCYAN_EX + ("*" * 120))
    for j in r:
        print(
            "%15s" % (Fore.MAGENTA + (str(j[0]))),
            "%34s" % (Fore.BLUE + (str(j[1]))),
            "%35s" % (Fore.LIGHTGREEN_EX + (str(j[2]))),
            "%20s" % (Fore.LIGHTYELLOW_EX + (str(j[3]))),
        )
    print(Fore.RESET)
    conn.close()


# UPDATING
def wrkupdate():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    ans = "y"
    while ans.lower() in "yes":
        wrkr = input("Enter worker id:").lower()
        print("Do you want to update salary(1) or job(2) or both(3) of", wrkr, "?")
        t = input("Enter choice:").lower()
        if t in "salary01":
            sal = int(input("Enter new salary:"))
            z = "update workers set sal='{}' where id = '{}'".format(sal, wrkr)
            cur.execute(z)
            conn.commit()
        elif t in "job02":
            jb = input("Enter new job title:")
            z = "update workers set job='{}' where id = '{}'".format(jb, wrkr)
            cur.execute(z)
            conn.commit()
        elif t in "both03":
            jb = input("Enter new job title:")
            sal = int(input("Enter new salary:"))
            z = "update workers set job='{}',sal='{}' where id = '{}'".format(jb, sal, id)
            cur.execute(z)
            conn.commit()
        ans = input("Are there anymore changes?:")
    conn.close()
    print("Data of specified worker(s) have been updated.")


def stkupdate():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    g = input("Enter stock id:")
    m = int(input("Enter units of stock left:"))
    cur = conn.cursor()
    cur.execute("update stock set unit ={} where id='{}'".format(m, g))
    conn.commit()
    conn.close()


def itupdate():
    conn = mysql.connector.connect(host=s[0], user=s[1], passwd=s[2], database=s[3])
    cur = conn.cursor()
    ans = "y"
    while ans.lower() in "yes":
        iname = input("Enter item name:").lower()
        pr = int(input("Enter new price:"))
        z = "update item set price='{}' where name like '{}'".format(pr, iname)
        cur.execute(z)
        conn.commit()
        ans = input("Do you want to update more item?:")
    conn.close()
    print("Specified item(s) have been updated.")   


# HEAD
def admin():
    print("\n1. Staff\n2. Stock\n3. Item\n4. Sell\n5. Exit")
    n = input("Enter choice:")
    if n == "1":
        print(
            "\n1. Add data new joines\n2. Update employee details\n3. Display details of employees\n4. Delete an employee's details\n"
        )
        z={1:wrkadd,2:wrkupdate,3:wrkdisp,4:wrkdlt}
        ni = int(input("Enter choice:"))
        for i in z.keys():
            if ni==i:
                z[i]()
    elif n == "2":
        print(
            "\n1. Add new stock purchase\n2. Update stock quantity\n3. Display stock\n4. Delete stock\n"
        )
        z = {1: stkadd, 2: stkupdate, 3: stkdisp, 4: stkdlt}
        ni = int(input("Enter choice:"))
        for i in z.keys():
            if ni == i:
                z[i]()
    elif n == "3":
        print("\n1. Add new item\n2. Update price\n3. Display menu")
        z = {1: itadd, 2: itupdate, 3: itdisp}
        ni = int(input("Enter choice:"))
        for i in z.keys():
            if ni == i:
                z[i]()
    elif n== "4":
        selldisp()        
    elif n == "5":
        print("Exiting the system.")
    else:
        print("Sorry! Such choice doesn't exist")
        admin()


def staff():
    print("\n1. Display your details\n2. Update stock\n3. Update item\n")
    z = {1: stdisp, 2: stkupdate, 3: itupdate}
    n = int(input("Enter choice:"))
    for i in z.keys():
        if n == i:
            z[i]()
