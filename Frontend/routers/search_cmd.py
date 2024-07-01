from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    first = State()

router = Router(name=__name__)


@router.message(Command('search'))
async def hadler_search(message: types.Message, state: FSMContext):
    await state.set_state(Form.first)
    await message.answer("What vacancy do you want  to search?")
    