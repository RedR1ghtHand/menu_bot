import sqlite3


def create_db():
    try:
        sql_con = sqlite3.connect('menu_data.db')
        create_table_menu = '''CREATE TABLE MENU_225 (
                                        id INTEGER PRIMARY KEY,
                                        dish TEXT NOT NULL,
                                        bot_command TEXT NOT NULL ,
                                        category TEXT NOT NULL,
                                        ingredients TEXT NOT NULL);'''

        cursor = sql_con.cursor()
        print('Connected')
        cursor.execute(create_table_menu)
        sql_con.commit()
        print('table created')

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        sql_con.close()
        print("connection is closed")


def add_colum():
    try:
        sql_con = sqlite3.connect('menu_data.db')
        add_colum_menu = """ALTER TABLE MENU_225 ADD COLUMN rating INTEGER"""

        cursor = sql_con.cursor()
        print('Connected')
        cursor.execute(add_colum_menu)
        sql_con.commit()
        print('column added!')

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        sql_con.close()
        print("connection is closed")



