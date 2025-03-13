from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import StatesGroup, State

from src.backend.search import searching_vac

class Time(StatesGroup):
    first = State()
    info_vacancy = State()

router = Router(name=__name__)
dictionary = {}
words_dic = {}

async def ikb_updated(text: str, num: int):
    keyboard = [
        [
            InlineKeyboardButton(text="<", callback_data="previous"),
            InlineKeyboardButton(text=f"{text}/{num}", callback_data="page"),
            InlineKeyboardButton(text=">", callback_data="next"),
        ]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inline_keyboard

@router.message(Command('info'))
async def handler_search(message: types.Message, state: FSMContext):
    await state.set_state(Time.first)
    await message.answer("О какой вакансии вы бы хотели получить больше информации?")

@router.message(Time.first)
async def procces_first(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Time.info_vacancy)

    id_user = message.from_user.id
    words_dic[id_user] = message.text
    dictionary[id_user] = 0
    vacancy_info = searching_vac(words_dic[id_user], query='all')
    vacancy_info_list = vacancy_info[dictionary[id_user]]
    
    await message.answer(text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}", reply_markup=await ikb_updated(text=f"{dictionary[id_user]}", num=len(vacancy_info)))


@router.callback_query(F.data == 'previous')
async def callback_previous(callback_query: CallbackQuery):
    id_user = callback_query.from_user.id
    vacancy = words_dic[id_user]
    vacancy_info = searching_vac(vacancy, query='all')

    if dictionary[id_user] == 0:
        vacancy_info_list = vacancy_info[len(vacancy_info)-1]

        await callback_query.message.edit_text(text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}",
                                                
        reply_markup=await ikb_updated(text=f"{len(vacancy_info)}", num=len(vacancy_info))
        )
        dictionary[id_user] = len(vacancy_info) - 1
    else:
        vacancy_info_list = vacancy_info[dictionary[id_user] - 1]

        await callback_query.message.edit_text(
            text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}",
                                               
         reply_markup=await ikb_updated(text=f"{dictionary[id_user] - 1}", num=len(vacancy_info))
         )
        dictionary[id_user] -= 1
    await callback_query.answer()


@router.callback_query(F.data == 'page')
async def callback_page(callback_query: CallbackQuery):
    await callback_query.answer(text="Текущая страница")


@router.callback_query(F.data == 'next')
async def callback_next(callback_query: CallbackQuery):
    id_user = callback_query.from_user.id
    vacancy = words_dic[id_user]
    vacancy_info = searching_vac(vacancy, query='all')

    if dictionary[id_user] == len(vacancy_info)-1:
        vacancy_info_list = vacancy_info[0]

        await callback_query.message.edit_text(text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}",
                                                
        reply_markup=await ikb_updated(text=f"{0}", num=len(vacancy_info))
        )
        dictionary[id_user] = 0
    else:
        vacancy_info_list = vacancy_info[dictionary[id_user]+1]

        await callback_query.message.edit_text(
            text=f"{vacancy_info_list[0]}\nГород: {vacancy_info_list[1]}\nЗанятость: {vacancy_info_list[2]}\nКомпания: {vacancy_info_list[3]}\nОпыт работы: {vacancy_info_list[4]}",
                                               
         reply_markup=await ikb_updated(text=f"{dictionary[id_user] + 1}", num=len(vacancy_info))
         )
            
        dictionary[id_user] += 1
    await callback_query.answer()    
