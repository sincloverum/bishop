import logging
from aiogram import Bot, Dispatcher, executor, types
from token import TOKEN
from words import WORDS

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def mess_handler(message: types.Message):
    text = message.text.lower()
    for word in WORDS:
        if word in text:
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