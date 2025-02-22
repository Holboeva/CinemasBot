from aiogram.fsm.state import StatesGroup, State


class SectorState(StatesGroup):
    movies_menu = State()
    drama_menu = State()
    movie_down = State()
    comedy_menu = State()
    action_menu = State()
    drama_movies = State()
    comedy_movies = State()
    action_movies = State()
    language = State()