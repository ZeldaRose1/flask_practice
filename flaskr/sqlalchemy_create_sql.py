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
    in_1 = sys.argv[1]
else:
    in_1 = None

# Turn off deprecation messages for a future version of SQL Alchemy
deprecations.SILENCE_UBER_WARNING = True

# Create engine
engine = sa.create_engine("sqlite:///main.db")

# Create inspector to check if tables exist
ins = sa.inspect(engine)

# Save first table query
t1_query = r"""
    CREATE TABLE test(
        id INTEGER PRIMARY KEY,
        genre NVARCHAR(100)
    );
"""

# Check if table already exists
if ins.has_table('test'):
    with engine.connect() as con:
        with con.begin():
            con.execute("DROP TABLE test")
            # Execute query
            if in_1 != '-d':
                con.execute(sa.text(t1_query))
else:
    with engine.connect() as con:
        con.execute(sa.text(t1_query))

# Clean query from memory
del t1_query

# Verify table is empty
if in_1 != '-d':
    with engine.connect() as con:
        # Check contents of test table
        result = con.execute(sa.text("select * from test"))
        # Check the result set is empty
        if result.rowcount == -1:
            print("Table 'test' successfully refreshed")
        else:
            print("Table 'test' could not be cleaned")
else:
    print("Tables successfuly deleted")
