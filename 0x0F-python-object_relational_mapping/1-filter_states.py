#!/usr/bin/python3
import sys
import MySQLdb

def connect_to_database(mysql_username, mysql_password, database_name):
    """
    Connects to the MySQL database with the provided credentials.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the MySQL database.

    Returns:
        MySQLdb.connections.Connection: MySQL database connection object.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        return db
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

def fetch_states_with_N(db):
    """
    Fetches and displays states with names starting with 'N' from the connected MySQL database.

    Args:
        db (MySQLdb.connections.Connection): MySQL database connection object.
    """
    try:
        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SELECT query to fetch states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor
        cursor.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = connect_to_database(mysql_username, mysql_password, database_name)

    fetch_states_with_N(db)

    db.close()
