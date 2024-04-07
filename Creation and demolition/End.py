import mysql.connector
import pickle
import os


s = []
with open("password.dat", "rb") as f:
    try:
        while True:
            s = pickle.load(f)
    except EOFError:
        pass


conn = mysql.connector.connect(host=s[0], database=s[3], user=s[1], passwd=s[2])
cur = conn.cursor()
cur.execute("drop database {}".format(s[3]))
os.remove("password.dat")
print("All data have been deleted successfully.")
