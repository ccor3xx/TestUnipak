from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тест'),
            KeyboardButton(text='Начало работы')
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите: '
)

def inline_btns():
    btns=[
        [
        InlineKeyboardButton(text='Работа в рамках СПЭП +', callback_data='inc1'),
        InlineKeyboardButton(text='Работа в рамках СПЭП -', callback_data='dec1')
    ],
    [InlineKeyboardButton(text='Назад', callback_data='back2')]
    ]
    kbd = InlineKeyboardMarkup(inline_keyboard=btns)
    return kbd

def inline_btns2():
    btns2=[
        [
        InlineKeyboardButton(text='Работа в рамках СПЭП +', callback_data='inc2'),
        InlineKeyboardButton(text='Работа в рамках СПЭП -', callback_data='dec2')
    ],
    [InlineKeyboardButton(text='Назад', callback_data='back2')]
    ]
    kbd2 = InlineKeyboardMarkup(inline_keyboard=btns2)
    return kbd2

def accept():
    bttn = InlineKeyboardButton(text='Записать', callback_data='accept')
    kbd1 = InlineKeyboardMarkup(inline_keyboard=bttn)
    return kbd1



