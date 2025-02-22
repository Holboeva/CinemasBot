from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_reply_button(texts, size, one_time_keyboard=False):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text= text) for text in texts])
    rkb.adjust(*size)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)


