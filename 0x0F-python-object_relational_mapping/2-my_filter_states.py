#!/usr/bin/python3
"""takes an argument and displays all values in the states table where name
matches the argument from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
