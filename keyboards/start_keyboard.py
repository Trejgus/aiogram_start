from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder

start_keyboard = InlineKeyboardBuilder(markup = [
    [
        InlineKeyboardButton(text = '/start' , callback_data = 'none'),
    ]
])

