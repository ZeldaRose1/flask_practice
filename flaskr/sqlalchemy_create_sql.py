#!/bin/python3

"""
    This script will create the tables needed for a project using Python
    and the SQL Alchemy package to control a SQL Lite database.

    Pass in -d in the command line to clean the tables
"""

# Import packages
import sys
import sqlalchemy as sa
# Import subpackage for setting parameters.
from sqlalchemy.util import deprecations

# Read input arguments
if len(sys.argv) > 1:
    database_name = sys.argv[1]

if len(sys.argv) > 2:
    in_2 = sys.argv[2]
else:
    in_2 = None

# Turn off deprecation messages for a future version of SQL Alchemy
deprecations.SILENCE_UBER_WARNING = True

# Create engine
engine = sa.create_engine(f"sqlite:///{database_name}")

# Create inspector to check if tables exist
ins = sa.inspect(engine)

# Save user table query
user_query = r"""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        username NVARCHAR(100),
        password NVARCHAR(100)
    );
"""

# Save reminder table query
reminder_query = r"""
    CREATE TABLE reminders(
        id INTEGER,
        category NVARCHAR(100),
        task_name NVARCHAR(100),
        alert_date DATE,
        description NVARCHAR(100),

        PRIMARY KEY (id, task_name),
        FOREIGN KEY (id) REFERENCES users(id)
    );
"""

# Initialize connection to interact with server
with engine.connect() as con:
    # Begin transaction
    with con.begin():
        # Remove users table before we try to recreate it
        if ins.has_table('users'):
            con.execute(sa.text("DROP TABLE users"))
        if in_2 != '-d':
            # Create users table if we aren't running a delete query
            con.execute(sa.text(user_query))

        # Remove reminders table before we recreate it.
        if ins.has_table('reminders'):
            con.execute(sa.text("DROP TABLE reminders"))
        # Create reminders table if we are not running a delete query
        if in_2 != '-d':
            con.execute(sa.text(reminder_query))

# Clean query from memory
del user_query
del reminder_query

# Verify users table is empty
if in_2 != '-d':
    with engine.connect() as con:
        # Check contents of users table
        result = con.execute(sa.text("SELECT * FROM users"))
        # Check the result set is empty
        if result.rowcount == -1:
            print("Table 'users' successfully refreshed")
        else:
            print("Table 'users' could not be cleaned")
else:
    print("Tables successfuly deleted")

# Verify reminders table is empty
if in_2 != '-d':
    with engine.connect() as con:
        # Check contents of reminders table
        result = con.execute(sa.text("SELECT * FROM reminders"))
        # Check the result set is empty
        if result.rowcount == -1:
            print("Table 'reminders' successfully refreshed")
        else:
            print("Table 'reminders' could not be cleaned")
else:
    print("Tables successfuly deleted")


# Add test users
in_query = r"""
    INSERT INTO USERS (id, username, password)
    VALUES (1, 'nancy', 'password');
"""

with engine.connect() as con:
    with con.begin():
        con.execute(sa.text(in_query))
        print("Appended test user to database")
