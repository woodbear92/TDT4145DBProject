import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilif180917",
    database="Project"
)


# Functional
def create_user(userName, email):
    mycursor = mydb.cursor()
    generatedKey = uuid.uuid1()
    id = generatedKey.bytes
    sql = "INSERT INTO User(UserID,UserName, UserEmail) VALUES (%s, %s, %s)"
    val = (id, userName, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Registered", userName)


# Functional
def show_users():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User ")
    userList = mycursor.fetchall()
    for user in userList:
        print(user)


def login():
    check_email=0
    print("Login")
    while not(check_email):
        email = input("Email: ")
        check_email = check_email_login(email)



# Functional
def create_login(email):
    passwrd = input("Provide a password: ")
    mycursor = mydb.cursor()
    sql = "INSERT INTO Login(UserEmail, Password) VALUES (%s, %s)"
    val = (email, passwrd)
    mycursor.execute(sql, val)
    mydb.commit()

#Functional
def check_email_login(email):
    mycursor = mydb.cursor()
    sql = 'SELECT useremail FROM login WHERE useremail = %s'
    val=(email,)
    mycursor.execute(sql,val)
    checkUserEmail = mycursor.fetchone()
    if checkUserEmail is not None:
        print('Email exists')
        return 1;
    else:
        print('Email does not exist! Try again')
    return 0
login()