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


def fetch_and_display_states(db):
    """
    Fetches and displays states from the connected MySQL database.

    Args:
        db (MySQLdb.connections.Connection): MySQL database connection object.
    """
    try:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id")

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        usage_message = (
            "Usage: {} < mysql_username > < mysql_password > < database_name >"
            .format(sys.argv[0])
        )
        print(usage_message)
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = connect_to_database(mysql_username, mysql_password, database_name)

    fetch_and_display_states(db)

    db.close()

