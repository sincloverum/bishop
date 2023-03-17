from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL

btnUrlChannel = InlineKeyboardButton(text='Перейти на канал Бишопа', url=CHANNEL_URL)
channel_menu = InlineKeyboardMarkup(row_width=1)
channel_menu.insert(btnUrlChannel)