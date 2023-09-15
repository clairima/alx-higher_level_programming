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


def fetch_states_by_name(db, state_name):
    """
    Fetches and displays states from the connected MySQL
    database where name matches the provided argument.

    Args:
        db (MySQLdb.connections.Connection):
        MySQL database connection object.
        state_name (str): State name to search for.
    """
    try:
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        usage_message = (
            "Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>"
            .format(sys.argv[0]))
        print(usage_message)
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = connect_to_database(mysql_username, mysql_password, database_name)

    fetch_states_by_name(db, state_name)

    db.close()

