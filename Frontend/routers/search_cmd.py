from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    first = State()
    sch_vacancy = State()

router = Router(name=__name__)


@router.message(Command('search'))
async def hadler_search(message: types.Message, state: FSMContext):
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

    await state.set_state(Form.first)
