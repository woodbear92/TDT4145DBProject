# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:52:29 2021

@author: Test
"""


import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="june92000",
    database="Project2"
)

#creates userID for testing
def uID(email):
    mycursor = mydb.cursor()
    sql = 'SELECT userID FROM user WHERE useremail = %s'
    val=(email,)
    mycursor.execute(sql,val)
    testID = (mycursor.fetchone())[0]
    return(testID)
    

# Functional
def create_user(userName, email, Instructor):
    mycursor = mydb.cursor()
    generatedKey = uuid.uuid4()
    id = generatedKey.bytes
    generatedKey = uuid.uuid4()
    PCID = generatedKey.bytes
   # (print(PCID))
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



##########for testing
def show_pcid():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User ")
    userList = mycursor.fetchall()
    for user in userList:
        print(get_pcid(user[0]),user[2])

def show_student():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT PCID FROM Student ")
    userList = mycursor.fetchall()
    for user in userList:
        print(user)
        
def show_instructor():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT PCID FROM instructor ")
    userList = mycursor.fetchall()
    for user in userList:
        print(user)
 ##############       


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

def get_user_PCID(userID):
    cur = mydb.cursor(buffered=(True),dictionary=True)
    cur.execute("SELECT * From student, instructor, user WHERE (user.UserID=student.StudentID or user.UserID = instructor.InstructorID) AND user.UserID = %s", (userID,))
    userinfo=cur.fetchone()
    pcid=userinfo["PCID"]
    return(pcid)


def get_pcid(UserID):
    if(check_student(UserID)):
        return((get_stud_PCID(UserID)))
    else:
        return((get_in_PCID(UserID)))
        
        
   

def check_student(userID):
    
    mycursor = mydb.cursor()
    sql = 'SELECT StudentID FROM student WHERE StudentID = %s'
    val=(userID,)
    mycursor.execute(sql,val)
    checkUser = mycursor.fetchone()
    if checkUser is not None:
        return 1
    else:
        return 0    
def check_instructor(userID):
    mycursor = mydb.cursor()
    sql = 'SELECT InstructorID FROM instructor WHERE InstructorID = %s'
    val=(userID,)
    mycursor.execute(sql,val)
    checkUser = mycursor.fetchone()
    if checkUser is not None:
        return 1
    else:
        return 0

def get_stud_PCID(userID):
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * From student, user WHERE (user.UserID=student.StudentID) AND user.UserID = %s", (userID,))
    userinfo=cur.fetchone()
    pcid=userinfo["PCID"]
    return(pcid)

def get_in_PCID(userID):
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * From instructor, user WHERE (user.UserID = instructor.InstructorID) AND user.UserID = %s", (userID,))
    userinfo=cur.fetchone()
    pcid=userinfo["PCID"]
    return(pcid)



def create_thread(postID, color, StudentReplyID, InstructorReplyID):
    mycursor = mydb.cursor()
    sql = "INSERT INTO thread(ThreadID, ThreadColor, StudentReplyID, InstructorReplyID) VALUES (%s, %s,%s, %s)"
    val = (postID, color, StudentReplyID, InstructorReplyID)
    mycursor.execute(sql, val)
    mydb.commit()

def create_tag(ThreadID, tag):
    mycursor = mydb.cursor()
    sql = "INSERT INTO tags(ThreadID, Tag) VALUES (%s, %s)"
    val = (ThreadID,tag)
    mycursor.execute(sql, val)
    mydb.commit()



def create_post(UserId):
    
    print("Thread: 1")
    print("Repy: 2")
    print("Discussion Post: 3")
    print("Exit any other input")
    post_selection = int(input("Type of post: "))
    
    if post_selection == 1:
        post_type = "Thread"
        #print(post_type)
    elif post_selection == 2:
        post_type = "Reply"
    elif post_selection == 3:
        post_type = "DiscussionPost"
    else:
        return
    
    post_content = input("Content: ")
    folder = input("Folder: ")
    tag = input("Tag: ")
    PCID=get_pcid(UserId)
    generatedKey = uuid.uuid4()
    postID = generatedKey.bytes
    
    #create post
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST(PostID, PostContent, PCID, PostType) VALUES (%s, %s,%s, %s) "
    val = (postID, post_content,PCID, post_type)
    mycursor.execute(sql, val)
    mydb.commit()

    create_thread(postID,0, None, None)
    create_tag(postID, tag)







