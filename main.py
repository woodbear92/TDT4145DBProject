import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilif180917",
    database="Project"
)


# Functional
def create_user(userName, email, Instructor):
    mycursor = mydb.cursor()
    generatedKey = uuid.uuid4()
    id = generatedKey.bytes
    generatedKey = uuid.uuid4()
    PCID = generatedKey.bytes
    sql = "INSERT INTO User(UserID,UserName, UserEmail) VALUES (%s, %s, %s)"
    val = (id, userName, email)
    mycursor.execute(sql, val)
    mydb.commit()
    if(Instructor):
        sql = "INSERT INTO PostCreator(PCID, CreatorType) VALUES (%s, %s)"
        val = (PCID, "Instructor")
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "INSERT INTO Instructor(InstructorId,PCID) VALUES (%s, %s)"
        val = (id, PCID)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        sql = "INSERT INTO PostCreator(PCID, CreatorType) VALUES (%s, %s)"
        val = (PCID, "Student")
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "INSERT INTO Student(StudentId,PCID) VALUES (%s, %s)"
        val = (id, PCID)
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

#Functional, solves use case 1?
def login():
    valid_email=0
    valid_password=0
    print("Login")
    while not(valid_email):
        email = input("Email: ")
        valid_email = check_email_login(email)
    while not (valid_password):
        password = input("Password: ")
        valid_password = check_password(email,password)



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
        return 1
    else:
        print('Email does not exist! Try again')
    return 0
#Functional
def check_password(email,password):
    mycursor = mydb.cursor()
    sql = 'SELECT useremail FROM login WHERE useremail = %s AND Password = %s'
    val = (email,password)
    mycursor.execute(sql, val)
    checkUserPassword = mycursor.fetchone()
    if checkUserPassword is not None:
        print('Password is valid')
        return 1
    else:
        print('Password is not valid! Try again')
    return 0
def create_post(UserId):
    print("Thread: 1")
    print("Repy: 2")
    print("Discussion Post: 3")
    print("Exit any other input")
    post_selection = input("Type of post: ")
    if post_selection == 1:
        post_type = "Thread"
    elif post_selection == 2:
        post_type = "Reply"
    elif post_selection == 3:
        post_type = "DiscussionPost"
    else:
        return
    post_content = input("Content: ")
    folder = input("Folder: ")
    tag = input("Tag: ")
create_user("Nick Fury", "FuryNicholasJ@gmail.com",1)




