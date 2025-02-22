
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from Bot.buttons.inline import pagination_inline_button
from Bot.buttons.reply import build_reply_button
from Bot.dispatcher import dp
from Bot.states import SectorState
from db.model import Movie


dramas = [Movie(id=1, title="Forrest Gump", year=1994, rating=8.8, image = "AgACAgIAAxkBAAEdK5ZnsaeCGtmxyoBi_QG1uxLzCJCEWwACG-8xG-KdiUmBsB-alDQwIwEAAwIAA3gAAzYE", descr="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
Movie(id=2, title="🎬 Titanic", year=1997, rating=8.5, image="AgACAgIAAxkBAAEdK7ZnsbJWfmzWfuBhDiQiVP4JM3u09gAC5_AxGw9yiEn1B8p29Pe8cgEAAwIAA3kAAzYE", descr="jkhigytfrydtesrxdcfvgnjk")]



@dp.message(SectorState.movies_menu, F.text == __("🎭 Drama"))
async def drama_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🎬 Forrest Gump"), _("🎬 Titanic"),  _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.drama_menu)
    await message.answer("🎥 Movies Menu", reply_markup=markup)


@dp.message(SectorState.drama_menu, F.text == __("🎬 Forrest Gump"))
async def drama_movie_handler(message: Message, state: FSMContext) -> None:
    first_movie = dramas[0]
    image = first_movie.image
    caption = (f"{_('Name')}: {first_movie.title}\n"
               f"{_('Year')}: {first_movie.year}\n"
               f"{_('Rating')}: {first_movie.rating}\n"
               f"{_('Description')}: {first_movie.descr}"
               )
    await state.set_state(SectorState.movie_down)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)

@dp.message( F.text == __("🎬 Titanic"))
async def drama_movie_handler(message: Message, state: FSMContext) -> None:
    second_movie = dramas[1]
    image = second_movie.image
    caption = (f"{_('Name')}: {second_movie.title}\n"
               f"{_('Year')}: {second_movie.year}\n"
               f"{_('Rating')}: {second_movie.rating}\n"
               f"{_('Description')}: {second_movie.descr}"
               )
    await state.set_state(SectorState.movie_down)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)
