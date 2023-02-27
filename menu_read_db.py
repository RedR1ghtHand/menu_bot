import sqlite3


def add_rating(dish: str, point=1):
    try:
        sqlite_con = sqlite3.connect('menu_data.db', timeout=20)
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_update_rating = """UPDATE MENU_225 SET rating = rating + {point}
                                     WHERE bot_command = '{dish}' """.format(dish=dish, point=point)

        cursor.execute(sqlite_update_rating)
        sqlite_con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def get_dish_rating() -> list:
    try:
        sqlite_con = sqlite3.connect('menu_data.db', timeout=20)
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT bot_command, rating from MENU_225
                                 ORDER BY rating DESC"""

        cursor.execute(sqlite_select_query)
        dish_by_rating = cursor.fetchmany(3)
        cursor.close()
        return dish_by_rating

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def get_ingredients(dish: str) -> str:
    try:
        sqlite_con = sqlite3.connect('menu_data.db', timeout=20)
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT ingredients from MENU_225
                                 WHERE bot_command = '{dish}' """.format(dish=dish)

        cursor.execute(sqlite_select_query)
        ingredients_dish = cursor.fetchone()
        cursor.close()
        return ingredients_dish[0]

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def get_dish_list(column) -> list:
    try:
        sqlite_con = sqlite3.connect('menu_data.db', timeout=20)
        cursor = sqlite_con.cursor()
        sqlite_select_query_dish = """SELECT {column_} from MENU_225""".format(column_=column)
        cursor.execute(sqlite_select_query_dish)
        dish_list = [item[0] for item in cursor.fetchall()]
        cursor.close()
        return dish_list

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def create_user_cart(_id: int):
    try:
        sqlite_con = sqlite3.connect('menu_data.db')
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_create_cart = f"""INSERT INTO user_cart (user_id, cart)
                                VALUES ({_id}, '')"""

        cursor.execute(sqlite_create_cart)
        sqlite_con.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def add_to_cart(_id: int, data: str):
    try:
        sqlite_con = sqlite3.connect('menu_data.db')
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_update_cart = f"""UPDATE user_cart
                                 SET cart = cart || '/{data}'
                                 WHERE user_id = {_id}
                                 """

        cursor.execute(sqlite_update_cart)
        sqlite_con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def get_user_cart(_id: int, type_of_return: str):
    try:
        sqlite_con = sqlite3.connect('menu_data.db', timeout=20
                                     )
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_create_cart = f"""SELECT cart FROM user_cart
                                 WHERE user_id = {_id}"""

        cursor.execute(sqlite_create_cart)
        data = cursor.fetchone()[0]
        sqlite_con.commit()
        cursor.close()

        user_cart = data.split('/')
        user_cart_dict = {item: user_cart.count(item) for item in user_cart if item != ''}
        user_cart_str = ''
        for item, count in user_cart_dict.items():
            user_cart_str += f'{item} : {str(count)}\n'

        if type_of_return == 'str':
            return user_cart_str
        elif type_of_return == 'dict':
            return user_cart_dict
        elif type_of_return == 'list':
            return user_cart[1::]

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def clear_user_cart(_id: int):
    try:
        sqlite_con = sqlite3.connect('menu_data.db')
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")

        sqlite_update_cart = f"""UPDATE user_cart
                                 SET cart = ''
                                 WHERE user_id = {_id}
                                 """

        cursor.execute(sqlite_update_cart)
        sqlite_con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        sqlite_con.close()
        print("The Sqlite connection is closed")


def calculate_menu(data):
    result = ''
    for dish in data:
        result += get_ingredients(dish)
    result = result.split('/')
    print(result)
    result_dict = {item: result.count(item) for item in result if item != ''}
    result_str = ''
    for item, count in result_dict.items():
        result_str += f'{item} : {str(count)}\n'
    return result_str



