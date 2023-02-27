from telebot import *
from telebot.callback_data import CallbackData
from menu_read_db import *




bot = telebot.TeleBot()
mrkp = None
menu_dict = dict(zip(get_dish_list('dish'), get_dish_list('bot_command')))
menu_factory = CallbackData('dish_id', prefix='dish')
user_id = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, tap /menu for start')
    global user_id
    user_id = message.chat.id
    create_user_cart(user_id)


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    category = types.KeyboardButton('/Категорії')
    food_rating = types.KeyboardButton('/Рейтинг')
    schedue = types.KeyboardButton('/Планувальник')

    markup.add(category, food_rating, schedue)
    bot.send_message(message.chat.id, 'Оберіть розділ 👇', reply_markup=markup)


@bot.message_handler(commands=['Рейтинг'])
def rating(message):
    dish_name = [item[0] for item in get_dish_rating()]
    dish_rating = [item[1] for item in get_dish_rating()]
    rating_list = f'ТОП 3 СТРАВ ПО ЗАПИТАМ:\n\n' \
                  f'{dish_name[0]}: {dish_rating[0]} запити(тів)\n\n' \
                  f'{dish_name[1]}: {dish_rating[1]} запити(тів)\n\n' \
                  f'{dish_name[2]}: {dish_rating[2]} запити(тів)\n\n'.format(dish_name=dish_name,
                                                                             dish_rating=dish_rating)

    bot.send_message(message.chat.id, rating_list)


@bot.message_handler(commands=['Категорії'])
def _category(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    susi = types.KeyboardButton('/Роли_Суші')
    meat = types.KeyboardButton("/М'ясні_страви")
    pasta = types.KeyboardButton('/Паста')
    side_dish = types.KeyboardButton('/Гарніри')
    pizza = types.KeyboardButton('/Піцка')
    burgers = types.KeyboardButton('/Бургери')
    breakfast = types.KeyboardButton('/Сніданки')
    wok = types.KeyboardButton('/Вок')
    back_to_menu = types.KeyboardButton('/menu')
    # seafood = types.KeyboardButton('/Морепродукти')

    markup.add(susi, meat, pasta, side_dish, pizza, burgers, breakfast, wok, back_to_menu)
    bot.send_message(message.chat.id, 'Оберіть категорію 👇', reply_markup=markup)


@bot.message_handler(commands=['Роли_Суші'])
def susi_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    nigiri = types.KeyboardButton('Гункани')
    o_nigiri = types.KeyboardButton('Онігірадзу')
    roll = types.KeyboardButton('Роли')
    back = types.KeyboardButton('/Категорії')

    markup.add(nigiri, o_nigiri, roll, back)
    bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


@bot.message_handler(commands=['Паста'])
def pasta_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    cream_pasta = types.KeyboardButton('Вершкова Паста')
    lasagna = types.KeyboardButton('Лазанья')
    carbonara = types.KeyboardButton('Карбонара')
    back = types.KeyboardButton('/Категорії')

    markup.add(cream_pasta, lasagna, carbonara, back)
    bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


# @bot.message_handler(commands=['Морепродукти'], content_types=["text", "photo"])
# def seafood_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#
#     salmon_bake = types.KeyboardButton('Лосось Запечений')
#     salmon = types.KeyboardButton('Сашимі')
#     tuna = types.KeyboardButton('Тунець')
#     back = types.KeyboardButton('/Категорії')
#
#     markup.add(salmon_bake, salmon, tuna, back)
#     bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


@bot.message_handler(commands=['Гарніри'])
def side_dish_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    potato_mashed = types.KeyboardButton('Пюре картопляне')
    potato_baked = types.KeyboardButton('Запечена картопля')
    ready_togo = types.KeyboardButton('Напівфабрикати')
    back = types.KeyboardButton('/Категорії')

    markup.add(potato_baked, potato_mashed, ready_togo, back)
    bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


@bot.message_handler(commands=['Піцка'])
def pizza_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    teriyaki = types.KeyboardButton('Курка-теріякі')
    seafood_pizza = types.KeyboardButton('Морепродукти')
    back = types.KeyboardButton('/Категорії')

    markup.add(teriyaki, seafood_pizza, back)
    bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


@bot.message_handler(commands=['Бургери'])
def burgers_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    classic_burger = types.KeyboardButton('Бургер класичний')
    chicken_burger = types.KeyboardButton('Бургер курячий')
    back = types.KeyboardButton('/Категорії')

    markup.add(classic_burger, chicken_burger, back)
    bot.send_message(message.chat.id, 'Оберіть страву 👇', reply_markup=markup)


@bot.message_handler(commands=['Сніданки'])
def breakfast_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


@bot.message_handler(commands=['Вок'], content_types=["text", "photo"])
def wok_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


@bot.message_handler(commands=['Планувальник'])
def scheduler(message):
    bot.send_message(message.chat.id, 'Ласкаво просимо до планувальника меню!\n'
                                      '1) оберіть список страв\n'
                                      '2) натисніть меню "РОЗРАХУВАТИ"\n'
                                      '3) бот розрахує для Вас перелік усіх інгредієнтів для готування та зручних покупок!')

    global mrkp
    mrkp = types.InlineKeyboardMarkup(row_width=2)

    calculate = types.InlineKeyboardButton(text='РОЗРАХУВАТИ', callback_data='calculate')
    clear = types.InlineKeyboardButton(text='Очистити кошик', callback_data='clear')

    mrkp.add(*[
                                              types.InlineKeyboardButton(
                                                  text=dish[1],
                                                  callback_data=menu_factory.new(
                                                      dish_id=dish[0]
                                                  )
                                              ) for dish in menu_dict.items()])
    mrkp.add(clear)
    mrkp.add(calculate)

    bot.send_message(message.chat.id, 'Оберіть страви зі списку:\nКорзина:', reply_markup=mrkp)
    clear_user_cart(message.chat.id)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_answers(callback):
    dish_data = callback.data[callback.data.find(':')+1::]
    if dish_data in get_dish_list('dish'):
        add_to_cart(callback.message.chat.id, data=menu_dict[dish_data])

        bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              reply_markup=mrkp,
                              text='Оберіть страви зі списку:\nКорзина:\n{user_cart}'
                              .format(user_cart=get_user_cart(callback.message.chat.id, type_of_return='str')))

    elif callback.data == 'calculate':
        calculate_ingredients = calculate_menu(get_user_cart(callback.message.chat.id, type_of_return='list'))
        bot.send_message(callback.message.chat.id, 'Розраховуємо інгредієнти:\n{result}'
                         .format(result=calculate_ingredients))

        clear_user_cart(callback.message.chat.id)

    elif callback.data == 'clear':
        clear_user_cart(callback.message.chat.id)
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              reply_markup=mrkp,
                              text='Оберіть страви зі списку:\nКорзина:')


@bot.message_handler(content_types=["text"])
def sub_menu(message):
    if message.text in get_dish_list('bot_command'):
        ingredients = get_ingredients(message.text)
        bot.reply_to(message, 'INGREDIENTS:\n' + ingredients.replace('/', '\n', ingredients.count('/')))
        add_rating(message.text)


bot.infinity_polling()
