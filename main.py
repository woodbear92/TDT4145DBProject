import mysql.connector
import uuid

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Eilif180917",
  database="Project"
)
#Functional
def create_user(userName, email):
    mycursor = mydb.cursor()
    generatedKey = uuid.uuid1()
    id = generatedKey.bytes
    sql = "INSERT INTO User(UserID,UserName, UserEmail) VALUES (%s, %s, %s)"
    val = (id,userName,email)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Registered", userName)
#Functional
def show_users():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User ")
    userList = mycursor.fetchall()
    for user in userList:
        print(user)
def login():
    print("Login")
    email = input("Email: ")
    mycursor = mydb.cursor()
    sql = "SELECT EXISTS(SELECT * FROM Login WHERE UserEmail = %s);"
    #This query doesnt seem to work.
    userEmail = (email,)
    registered = mycursor.execute(sql,email)

    print(registered)
#Functional
def create_login(email):
    passwrd = input("Provide a password: ")
    mycursor = mydb.cursor()
    sql = "INSERT INTO Login(UserEmail, Password) VALUES (%s, %s)"
    val = (email,passwrd)
    mycursor.execute(sql, val)
    mydb.commit()
login()
