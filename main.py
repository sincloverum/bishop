import logging
import markups as nav
from aiogram import Bot, Dispatcher, executor, types
from tokens import TOKEN
from words import WORDS
from config import CHANNEL_ID


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

def chech_sub_channel(chat_member):
    return chat_member['status'] != 'left'

@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message: types.Message):
    await message.answer('Привет!\nМы тебе рады!\n✔️Мы будем вынуждены удалять всех, кто не представляется в чате, кого мы не можем идентифицировать — ради нашей общей безопасности. ✔️Представься, пожалуйста, если хочешь остаться в группе\n♥️ Это нужно сделать ОДИН раз, мы вас запишем, и вы навсегда останетесь в чате.\n❗️Если ты первый раз в группе Анонимных Алкоголиков — напиши, что ты «новичок»')

@dp.message_handler()
async def mess_handler(message: types.Message):

    if chech_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        text = message.text.lower()
        for word in WORDS:
            if word in text:
                await message.delete()
    else:
        await message.answer('Тебе следует подписаться на канал Бишопа, бро. Перед тем, как оставлять свои комменты здесь', reply_markup=nav.channel_menu)
        await message.delete()

"""
#Узнать ID 
@dp.message_handler(commands='idanswer', commands_prefix='/')
async def test(message=types.Message):
    await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}")
    
#Приветствие
@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message: types.Message):
    await message.answer('Привет!\nМы тебе рады!\n✔️Мы будем вынуждены удалять всех, кто не представляется в чате, кого мы не можем идентифицировать — ради нашей общей безопасности. ✔️Представься, пожалуйста, если хочешь остаться в группе\n♥️ Это нужно сделать ОДИН раз, мы вас запишем, и вы навсегда останетесь в чате.\n❗️Если ты первый раз в группе Анонимных Алкоголиков — напиши, что ты «новичок»')
"""

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)