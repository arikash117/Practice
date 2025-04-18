from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from backend.search import searching_vac

class Form(StatesGroup):
    first = State()
    sch_vacancy = State()

router = Router(name=__name__)


@router.message(Command('search'))
async def handler_search(message: types.Message, state: FSMContext):
    await state.set_state(Form.first)
    await message.answer("Какую вакансию вы хотите найти?")


@router.message(Form.first)
async def process_first(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.sch_vacancy)

    vacancy_list = searching_vac(message.text, query=None)
    await message.answer(f"Нашлось {len(vacancy_list)} вакансий, Вот они:\n{'\n'.join(vacancy_list)}")
    
    await state.clear()
