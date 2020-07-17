# #############################################################
# SQLite File Reading Adapter.
# ========

# TODO


# Features
# --------

# - Make Interacting with SQLite files easier.
# - Execute Custom SQL Commands

# Usage
# -----

# db_adapter = sqlite_adapter("database_file.db")
# db_adapter.table = "table1"
# db_adapter.retrieve_data("column1", "column2")
# db.db_adapter.execute("SELECT * FROM `table1`")

# Contribute
# ----------

# - Issue Tracker: ghttps://github.com/neatphar/product_recommendation_system/issues
# - Source Code: https://github.com/neatphar/product_recommendation_system

# Support
# -------

# If you are having issues, please let me know.
# at: neatphar@gmail.com

# License
# -------

# The project is licensed under the GNU GENERAL PUBLIC LICENSE.

# #############################################################

import sqlite3 as sql
from os.path import exists

class sqlite_adapter():
    __conn, __selected_table = None, None

    def __init__(self, db_file_name):
        if not exists(db_file_name):
            raise Exception("File not found.")
        self.__conn = sql.connect(db_file_name)
        #print("SQLite file initialized successfully.")

    def execute(self, sql_string):
        if self.__selected_table == None:
            raise Exception("Table is not found.")
        return self.__conn.execute(sql_string), self.__conn.commit()

    def retrieve_data(self, *args):
        cursor, _ = self.execute("SELECT `{}` from {}".format("`, `".join(args), self.__selected_table))
        return [i for i in cursor]

    @property
    def table(self):
        return self.__selected_table
    
    @table.setter
    def table(self, table_name):
        rows = self.__conn.execute("SELECT count(*) FROM `sqlite_master` WHERE type='table' AND name='{}'".format(table_name))
        if not rows.fetchone()[0]:
            raise Exception("Table is not found.")
        #print("Selected table is changed from `{}` to `{}` successfully.".format(self.__selected_table, table_name))
        self.__selected_table = table_name

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()







