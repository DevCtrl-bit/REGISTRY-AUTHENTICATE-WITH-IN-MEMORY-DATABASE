import sqlite3

db = sqlite3.connect(":memory:")
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Users (
                id integer PRIMARY KEY,
                username varchar(255),
                password varchar(255) )''')


def userNameSet():

    try:
        username = input("Please add an Username: ")
    except:
        print("Something went wrong.")
        userNameSet()

    return username

def passSet():

    try:
        password = input("Add a password:")
    except:
        print("Something went wrong.")
        passSet()

    return password

#checkData es FUNCION UNICAMENTE DE PRUEBA PARA VER DB INFO

def checkData():

    query = """
         INSERT INTO Users
             (username, password)
         VALUES
              (?, ?)
            """
    data =  [user, passw]

    cur.execute(query, data)


print("WELCOME, please register yourself to continue...")
a = input("Wanna CHECK data or BEGIN?:")

if a == "BEGIN":

    user = userNameSet()
    passw = passSet()

elif a == "CHECK":

    checkData()


print("LOGIN to check your email:")
