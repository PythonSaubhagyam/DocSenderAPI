# from traceback import print_tb
# import pytesseract
# import os
# from PIL import Image
# path ="/home/parth/Documents/DocSenderAPI/images"
# def ocr_core():
#     for imageName in os.listdir(path):
#         inputPath = os.path.join(path, imageName)
#         img = Image.open(inputPath)
#         text =pytesseract.image_to_string(img)
#         print(text)
#         # print(text)# We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
#     # return text
# ocr_core()
# from mysql.connector.constants import ClientFlag
import mysql.connector

# mydb =  mysql.connector.connect(
# 	host = "localhost",
# 	database='docsender_db',
#     port = 3306,
# 	user = "doc_admin",
# 	password = "Admin123!@#"
# )
# cursor = mydb.cursor()
# print(cursor)


# conn = MySQLdb.connect("host", "user", "password", "database")

from sqlalchemy import create_engine



username = 'doc_admin'
password = 'Admin123!#'
host = 'localhost'
port = 3306
DB_NAME = 'db_name'

# engine = create_engine('mysql://{username}:{password}@{host}:{port}')
# engine = create_engine('mysql+pymysql://doc_admin:Admin123!#@184.168.96.176/docsender_db')\
# engine = create_engine('mysql+pymysql://db_user:db_user_pass@172.21.0.3/cart', pool_recycle=3600)
# engine = create_engine('mysql+pymysql://doc_admin:Admin123!#@localhost')

# Creating connection object
# mydb =  mysql.connector.connect(
# 	host = "localhost",
# 	database='minipokemart',
# 	user = "doc_admin",
# 	password = "Admin1234!#$"
# )
# cursor = mydb.cursor()
sqlEngine = create_engine('mysql+pymysql://doc_admin:Admin1234!#$@localhost:3306/docsender_db', pool_recycle=3600)
dbConnection = sqlEngine.connect()
# conn = engine.connect()
# import sqlalchemy
# engine = sqlalchemy.create_engine('mysql://doc_admin:Admin123!@#@sg2plzcpnl466820.prod.sin2.secureserver.net')
# print(engine)
# engine.connect()