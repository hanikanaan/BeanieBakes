from aifc import Error

import sqlparse as sp
import globalvars as gv
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect('db.sqlite3')
    except Error as e:
        print(e)


def result():
    searchresult = ''


def main():
    sp.parse(gv.searchstring)
    result()


if __name__ == '__main__':
    main()
