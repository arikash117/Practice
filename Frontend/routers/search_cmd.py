from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from Backend.main import searching_vac

class Form(StatesGroup):
    first = State()
    sch_vacancy = State()

router = Router(name=__name__)


@router.message(Command('search'))
async def handler_search(message: types.Message, state: FSMContext):
    await state.set_state(Form.first)
    await message.answer("What vacancy do you want  to search?")


@router.message(Form.first)
async def procces_first(message: types.Message, state: FSMContext):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    await state.update_data(name=message.text)
    await state.set_state(Form.sch_vacancy)
    vacancy_list = searching_vac(message.text)
    await message.answer(f"Look i found {len(vacancy_list)} vacancies, here they are:\n{'\n'.join(vacancy_list)}")
    await state.set_state(Form.first)
