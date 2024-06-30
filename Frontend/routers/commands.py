from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


router = Router(name=__name__)


@router.message(Command('start'))
async def handler_start(message: types.Message):
    keyboard = [
        [KeyboardButton(text="/start")],
        [KeyboardButton(text='/help')],
        [KeyboardButton(text='/search')],
        [KeyboardButton(text='/cancel')],
    ]

    ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.reply(text='Hi! This is your helper for searching hh.ru vacancies!!! Type /help for for help)')
    await message.reply_sticker(sticker='CAACAgIAAxkBAAEGizlmgZbS7tRx_pTFXwcxi6hvjY9VDgACAQEAAladvQoivp8OuMLmNDUE')
