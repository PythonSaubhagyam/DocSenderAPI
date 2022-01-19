import mysql.connector

mydb = mysql.connector.connect(
	host = "34.145.247.58",
	user="db_user",
    port=8081,
	password="db_user_pass",
	database="app_db"
	)
	
print(mydb)