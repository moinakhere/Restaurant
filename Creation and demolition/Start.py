import pickle
import mysql.connector
from colorist import BrightColor

with open("password.dat", "ab") as f:
    a = input("Enter host:")
    b = input("Enter user:")
    cs = input("Enter connection password:")
    d = input("Enter database:")
    e = input("Enter admin entry pin:")
    g = input("Enter staff entry pin:")
    if (a.isalnum() and b.isalnum() and d.isalnum()):
        z=[a,b,cs,d,e,g]
        pickle.dump(z, f)

    else:
        z=["localhost","root","rst",cs,e,g]
        pickle.dump(z,f)


if a.isalnum() and b.isalnum():
    conn = mysql.connector.connect(host=a, user=b, passwd=cs)
else:
    conn = mysql.connector.connect(host="localhost", user="root", passwd=cs)
cur = conn.cursor()
curx = conn.cursor()


if d.isalnum():
    cur.execute("create database if not exists {}".format(d))
else:
    cur.execute("CREATE DATABASE if not exists rst")
if d.isalnum():
    cur.execute("USE {}".format(d))
else:
    cur.execute("USE rst")


cur.execute(
    "create table if not exists Item(No int(4) not null auto_increment primary key, Name varchar(225) not null,Type varchar(225) not null, Price float(7,2) not null)"
)
cur.execute(
    "create table if not exists workers(Code varchar(2) not null primary key,Name varchar(225) not null,Job varchar(225) not null,Sal int(10))"
)
cur.execute(
    "create table if not exists Stock(Id varchar(10) not null primary key, Name varchar(237), Unit_price float(6,2) not null, Unit int not null)"
)
cur.execute(
    "create table if not exists Sell(Date date not null, Time varchar(100) not null, Sell float(6,2))"
    )
cur.execute(
        "insert into workers values('Ab','Ayesha Khan','General Manager',60000),('Ba','Arjun Sharma','Assistant Manager',45000),('Ac','Fatima Ali','Operations Manager',50000),('Ca','Sameer Ahmed','Restaurant Supervisor',40000),('Ad','Priya Patel','Shift Manager',35000),('Da','Rajesh Singh','Head Chef',70000),('Ae','Mariam Khan','Sous Chef',55000),('Ea','Amir Khan','Indian Cuisine Line Cook',30000),('Af','Farida Baig','Pakistani Cuisine Line Cook',30000),('Fa','Rahul Verma','Tandoor Chef',40000),('Ag','Anjali Gupta','Prep Cook',25000),('Ga','Kamal Das','Dishwasher',20000),('Ah','Natasha Sharma','Restaurant Captain',35000),('Ha','Rahul Mehta','Waiter',22000),('Ai','Simran Kaur','Waitress',22000),('Ia','Karan Patel','Host',18000),('Aj','Reema Singh','Bartender',27000),('Ja','Aman Verma','Busser',15000),('Ak','Nisha Mehra','Front-of-House Manager',45000),('Ka','Vikram Kapoor','Dining Room Manager',40000),('Al','Priyanka Reddy','Beverage Manager',35000),('La','Vivek Menon','Kitchen Manager',50000),('Am','Jaya Rao','Inventory Manager',40000),('Ma','Deepak Joshi','Purchasing Manager',45000),('An','Ramesh Iyer','Accountant',40000),('Na','Sunita Sharma','Human Resources Manager',45000),('Ao','Devika Desai','Office Administrator',30000),('Oa','Aarti Mehta','Training Manager',45000),('Ap','Vikas Singh','Staff Trainer',25000),('Pa','Danish Khan','Delivery Manager',40000),('Aq','Ajay Verma','Delivery Driver',22000),('Qa','Ankit Malhotra','Legal Advisor',60000),('Ar','Neha Iyer','Compliance Officer',45000)"
        )
cur.execute(
        "insert into Item values (0,'Chicken Seekh Kebab','Starters',75),(0,'Tandoori Rooti','Roti',40),(0,'Pani Puri','Starters',80),(0,'Fish Pakora','Starters',180),(0,'Aloo Tikki Chaat','Starters',70),(0,'Tandoori Mushroom','Starters',120),(0,'Paneer Tikka','Starters',130),(0,'Mulligatawny Soup','Soup',80),(0,'Chicken Corn Soup','Soup',100),(0,'Kachumber Salad','Salad',70),(0,'Dal Shorba','Soup',60),(0,'Green Papaya Salad','Salad',90),(0,'Vegetable Biryani','Vegetarian Main Course',180),(0,'Shahi Paneer','Vegetarian Main Course',160),(0,'Palak Paneer','Vegetarian Main Course',140),(0,'Baingan Bharta','Vegetarian Main Course',120),(0,'Vegetable Jalfrezi','Vegetarian Main Course',130),(0,'Chicken Biryani','Non-Vegetarian Main Course',220),(0,'Rogan Josh','Non-Vegetarian Main Course',200),(0,'Butter Chicken','Non-Vegetarian Main Course',240),(0,'Garlic Naan','Naan',40),(0,'Lachha Paratha','Paratha',30),(0,'Onion Kulcha','Kulcha',50),(0,'Aloo Paratha','Paratha',40),(0,'Roomali Roti','Roti',35),(0,'Tadka Dal','Dal',80),(0,'Raita','Sides',40),(0,'Rose Sherbet','Beverages',45),(0,'Gulab Jamun','Desserts',50),(0,'Kheer','Desserts',80),(0,'Mango Kulfi','Desserts',55),(0,'Nalli Nihari','Chef special',280),(0,'Chicken Haleem','Chef special',200),(0,'Bhuna Gosht','Chef special',250),(0,'Special Mix Grill Platter','Chef special',300)"
        )
cur.execute(
        "insert into stock values('A0','Basmati Rice',10.00,100),('B1','Chicken',5.50,50),('C2','Lamb Meat',8.00,30),('D3','Paneer',6.00,20),('E4','Mixed Vegetables',2.50,80),('F5','Lentils',3.00,40),('G6','Spices',1.50,10),('H7','Wheat Flour',4.00,60),('I8','Besan',3.00,25),('J9','Yogurt',2.00,30),('K0','Cooking Oil',15.00,40),('L1','Garlic',1.20,15),('M2','Ginger',2.00,10),('N3','Green Chilies',1.80,8),('O4','Fresh Herbs',2.50,5),('P5','Mustard Seeds',3.50,3),('Q6','Fenugreek Leaves',4.00,4),('R7','Tamarind',7.00,2),('S8','Cashew Nuts',12.00,8),('T9','Almonds',10.00,10),('U0','Cardamom',15.00,3),('V1','Cloves',10.00,5),('W2','Bay Leaves',5.00,2),('X3','Black Pepper',8.00,4),('Y4','Red Chili Powder',6.00,6),('Z5','Saffron',100.00,0.5),('A6','Vinegar',3.00,5),('B7','Coconut Milk',4.00,15),('C8','Safflower Oil',10.00,10),('D9','Ghee',20.00,12),('E0','Jaggery',5.00,5),('F1','Curry Leaves',4.00,2),('H3','Seafood',14.00,23)"
        )

conn.commit()
conn.close()
print(f"{BrightColor.CYAN}All good to begin with.{BrightColor.OFF}")
