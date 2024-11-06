#!/bin/python3

import sys
import os

import pytest
import sqlalchemy as sa

def test_create_tables():
    """ This test verifies the create tables function makes the tables"""
    os.system(os.path.join("..", "flaskr", "sqlalchemy_create_sql.py") + " test.db")

    # Create engine
    engine = sa.create_engine("sqlite:///test.db")

    # Create inspector to check if tables exist
    ins = sa.inspect(engine)

    # Test for the proper tables
    assert 'reminders' in ins.get_table_names()
    assert 'users' in ins.get_table_names()

    # Pull and test users table columns
    users_cols = ins.get_columns("users")
    assert users_cols[0]['name'] == 'id'
    assert isinstance(users_cols[0]['type'], sa.INTEGER)

    assert users_cols[1]['name'] == 'username'
    assert isinstance(users_cols[1]['type'], sa.NVARCHAR)

    assert users_cols[2]['name'] == 'password'
    assert isinstance(users_cols[2]['type'], sa.NVARCHAR)

    # Pull and test reminders table columns
    rm_cols = ins.get_columns("reminders")
    assert rm_cols[0]['name'] == 'id'
    assert isinstance(rm_cols[0]['type'], sa.INTEGER)

    assert rm_cols[1]['name'] == 'category'
    assert isinstance(rm_cols[1]['type'], sa.NVARCHAR)

    assert rm_cols[2]['name'] == 'task_name'
    assert isinstance(rm_cols[2]['type'], sa.NVARCHAR)

    assert rm_cols[3]['name'] == 'alert_date'
    assert isinstance(rm_cols[3]['type'], sa.DATE)

    assert rm_cols[4]['name'] == 'description'
    assert isinstance(rm_cols[4]['type'], sa.NVARCHAR)

    # Clean up database
    os.remove('test.db')

def test_delete_tables():
    """ This test verifies the create tables function makes the tables"""
    os.system(os.path.join("..", "flaskr", "sqlalchemy_create_sql.py") + " test.db")
    os.system(os.path.join("..", "flaskr", "sqlalchemy_create_sql.py") + " test.db -d")

    # Create engine
    engine = sa.create_engine("sqlite:///test.db")

    # Create inspector to check if tables exist
    ins = sa.inspect(engine)

    assert len(ins.get_table_names()) == 0

    # Clean up database
    os.remove('test.db')

