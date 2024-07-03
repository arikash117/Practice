from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from .search_cmd import Form
from ...Backend.main import searching_vac

router = Router(name=__name__)
dictionary = {}

async def ikb_updated(text: str):
    keyboard = [
        [
            InlineKeyboardButton(text="<", callback_data="previous"),
            InlineKeyboardButton(text="f{text}/{num}", callback_data="page"),
            InlineKeyboardButton(text=">", callback_data="next"),
        ]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inline_keyboard

@router.message(Command('info'))
async def handler_search(message: types.Message, state: FSMContext):
    await state.set_state(Form.first)
    id_user = message.from_user.id
    dictionary[id_user] = 0
    await message.answer("About which vacancy you want to see more information?")

@router.message(Form.first)
async def procces_first(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.info_vacancy)
    vacancy_info_list = searching_vac(message.text, query='all')
    await message.answer(
        f""
    )
