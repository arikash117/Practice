from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


router = Router(name=__name__)


@router.message(Command('start'))
async def handler_start(message: types.Message):
    keyboard = [
        [KeyboardButton(text="/start")],
        [KeyboardButton(text='/help')],
        [KeyboardButton(text='/search')],
        [KeyboardButton(text='/cancel')],
        [KeyboardButton(text='/info')],
    ]

    ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.reply(text='Здравствуйте, это ваш бот-помощник для поиска ваканский! Вывести справку - /help)')
    await message.reply_sticker(sticker='CAACAgIAAxkBAAEGizlmgZbS7tRx_pTFXwcxi6hvjY9VDgACAQEAAladvQoivp8OuMLmNDUE')



@router.message(Command('help'))
async def handler_help(message: types.Message):
    await message.reply(text="This is command list"
                        "\n/start - запустить бота"
                        "\n/help - вызвать справку"
                        "\n/cancel - отменить текущее действие"
                        "\n/search - найти вакансии по запросу"
                        "\n/info - получить информацию о вакансиях"
                        )


@router.message(Command('cancel'))
async def cancel_cmd(message: types.Message, state: FSMContext):
    current_state = state.set_state()
    if current_state is None:
        return
    await message.reply('Отменено')
    await state.clear()
