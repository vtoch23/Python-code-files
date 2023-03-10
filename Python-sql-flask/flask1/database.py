import sqlite3

def dbcon():
    return sqlite3.connect("names.db", check_same_thread=False)