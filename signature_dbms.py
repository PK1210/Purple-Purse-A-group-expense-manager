import sqlite3 as sql

def create_connection(database):
    try:
        conn = sql.connect(database)
        return conn;
    except:
        print "Cannot access database"

def insertUser(name,email,password):
    conn = create_connection("database.db")
    curr = conn.cursor()
    try:
        curr.execute("INSERT INTO USERS (name,email,password) VALUES(?,?,?)",(name,email,password))
    except sql.IntegrityError as e:
        print("Account already exists")
        return 0
    conn.commit()
    conn.close()
    return 1

def findUserByUser_Id(id):
    query = None
    conn = create_connection("database.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM USERS WHERE user_id is '{}'".format(id))
    query = curr.fetchone()
    conn.close()
    print query
    return query

def findUserByEmail(email):
    query=None
    conn = create_connection("database.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM USERS WHERE email = '{}'".format(email))
    query = curr.fetchone()
    conn.close()
    return query

def retrieveUsers():
	conn = create_connection("database.db")
	curr = conn.cursor()
	curr.execute("SELECT name, email,password FROM USERS")
	users = curr.fetchall()
	conn.close()
	return users
