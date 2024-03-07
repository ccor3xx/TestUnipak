from aiogram.fsm.state import State, StatesGroup


class Botver1(StatesGroup):
    fact1 = State()
    fact2 = State()
    accept = State()