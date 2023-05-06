from aiogram import Bot , Dispatcher , html , F
from aiogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from aiogram.filters.command import Command
from aiogram.filters import CommandObject , Text 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.fsm.state import StatesGroup , State 
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand , BotCommandScope , BotCommandScopeAllGroupChats
from aiogram.enums import ContentType , ChatType  


import logging
import asyncio

# HANDLERS
from handlers.start_handler import start_handler
from handlers.admin import admin

bot = Bot('5223153520:AAEhoka4frLhOH6efQz7C68Wl5dvAtIur54')
dp = Dispatcher()



@dp.message(Command('start'))
async def start_cmd(message:Message):
    await message.answer('Hello World')
    
# <---YOUR HANDLERS--->
  
async def main():
    
    async def startup_message():
        print('Bot running!')  
    # <---ROUTERS--->
    dp.include_routers(start_handler.router)
    dp.include_router(admin.router)
    # <---END--->
    dp.startup.register(startup_message)  
    await dp.start_polling(bot) 
   
if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG ,
                        filename = 'log.log' ,
                        filemode = 'w',
                        format = '%(asctime)s %(levelname)s %(message)s')
    asyncio.run(main()) 