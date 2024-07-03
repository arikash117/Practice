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
    await message.answer("О какой вакансии вы бы хотели получить больше информации?")

@router.message(Form.first)
async def procces_first(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.info_vacancy)

    id_user = message.from_user.id
    dictionary[id_user] = 0
    vacancy_info = searching_vac(message.text, query='all')
    vacancy_info_list = vacancy_info[id_user]
    await message.answer(text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}")


@router.callback_query(F.data == 'previous')
async def callback_previous(callback_query: CallbackQuery):
    id_user = callback_query.from_user.id
    vacancy = callback_query.message.id
    if dictionary[id_user] == 0:
        vacancy_info = searching_vac(vacancy, query='all')
        await callback_query.message.edit_text(

        )
