#!/usr/bin/python3
"""
    MYSQL Script
"""
import mysql.connector
from mysql.connector import Error

def create_mysql_connection(host, user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("MySQL Database connection successful")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def create_database(connection, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created successfully")
    except Error as e:
        print(f"Error creating database: {e}")

def create_user(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE USER IF NOT EXISTS '{username}'@'localhost' IDENTIFIED BY '{password}'")
        print(f"User '{username}' created successfully")
    except Error as e:
        print(f"Error creating user: {e}")

def grant_privileges(connection, username, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{username}'@'localhost'")
        cursor.execute(f"GRANT SELECT ON performance_schema.* TO '{username}'@'localhost'")
        print("Privileges granted successfully")
    except Error as e:
        print(f"Error granting privileges: {e}")

def main():
    # Modify these values with your MySQL server details
    host = 'localhost'
    user = 'root'
    password = 'Slonjoh'
    db_name = 'solysis_dev_db'
    username = 'solysis_dev'
    user_password = 'solysis_dev_pwd'

    # Create MySQL connection
    connection = create_mysql_connection(host, user, password)
    if not connection:
        return

    # Create database
    create_database(connection, db_name)

    # Create user
    create_user(connection, username, user_password)

    # Grant privileges
    grant_privileges(connection, username, db_name)

    # Close connection
    connection.close()

if __name__ == "__main__":
    main()
