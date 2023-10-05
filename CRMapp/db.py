# Importing mysql connector
import mysql.connector

# Establishing connection
database = mysql.connector.connect(host="localhost", user="root", password="arsalan")

# Getting cursor object
cursor = database.cursor()

cursor.execute("CREATE DATABASE Djpractice")

print("All Done!")