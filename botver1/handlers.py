from random import randint
# import json
from aiogram import types, Router, F
from aiogram.filters import or_f, Command
from aiogram.fsm.context import FSMContext

from states import Botver1
from aiogram.utils.keyboard import InlineKeyboardBuilder

from botver1.kbds import inline_btns, inline_btns2 # accept,
from load_json import head, answer, spep, video

user_router = Router()

first_item = (f'{answer['last_name']}' f' {answer['first_name']}') #f'{answer['managers']['id_managers_name']['name']}' f'{answer['managers']['factors']}'
second_item = 'ТФК: '  f'{head['id_work_item']['id_GN']['name']}'
third_item = 'Материал: ' f'{head['id_work_item']['id_item']['name']}'
fourth_item = 'Отклонение в продукции: ' f'{head['id_overrun_pieces']['name']}'
fifth_item = 'Отклонение в материале: ' f'{head['id_overrun_pieces']['name']}'
sixth_item = 'Факторы: '
seventh_item = f'\n{spep}' f'\n{video}'

shapka = f'{f'{first_item}'
                         f'\n{second_item}\n'
                         f'\n{third_item}\n'
                         f'\n{fourth_item}\n'
                         f'\n{fifth_item}\n'
                         f'\n{sixth_item}'}'

@user_router.message(or_f(Command('work'), (F.text.lower() == 'начало работы')))
async def cmd_help(message: types.Message, state: FSMContext):
    await state.set_state(Botver1.fact1)
    await message.answer(f'{shapka}' + f'{seventh_item}', reply_markup=inline_btns())


@user_router.message(or_f(Command('check'), (F.text.lower() == 'тест')))
async def cmd_check(message: types.Message):
    await message.answer_dice()

@user_router.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 100",
        reply_markup=builder.as_markup()
    )
@user_router.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 100)))


@user_router.callback_query(Botver1.fact1)
async def action_callback(call: types.CallbackQuery, state: FSMContext):
    global spep
    global video
    await state.set_state(Botver1.fact1)
    if call.data == "inc1":
        spep += "+"
    elif call.data == "dec1":
        spep += "-"
    elif call.data == "back1":
        await call.answer(text="Там ничего нет", show_alert=True)
    await call.message.edit_text(f'{shapka}' f'\n{spep}||' f'\n{video}', reply_markup=inline_btns())
    await state.update_data(fact1=spep, video=video)
    await state.set_state(Botver1.fact2)

@user_router.callback_query(Botver1.fact2)
async def action_callback2(call: types.CallbackQuery, state: FSMContext):
    global video
    global spep
    if call.data == "inc2":
        video += "+"
    elif call.data == "dec2":
        video += "-"
    elif call.data == "back2":
        await state.set_state(Botver1.fact1)
        await call.message.edit_text(f'{shapka}' f'\n{spep}||' f'\n{video}', reply_markup=inline_btns2())
    await state.update_data(fact2=video, spep=spep)
    await call.message.edit_text(f'{shapka}' f'\n{spep}' f'\n{video}||', reply_markup=inline_btns2())

