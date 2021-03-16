
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Eilif180917",
  database="Project"
)

def create_user(id,userName, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO User(UserID,UserName, UserEmail) VALUES (%s, %s, %s)"
    val = (id,userName,email)
    mycursor.execute(sql,val)

    mydb.commit()
def show_users():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM User    ")
    userList = mycursor.fetchall()
    for user in userList:
        print(user)
# create_user("user1","email@email.com")
show_users()


