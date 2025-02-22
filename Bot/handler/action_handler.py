
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

actions = [Movie(id=1, title="🎬 John Wick", year=2014, rating=8.8, image = "AgACAgIAAxkBAAEdK9NnsbvcTN_ex3OLjBrdgoHCv8_6yQACy-8xG-KdiUnzVrNV14mhVAEAAwIAA3gAAzYE", descr="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
Movie(id=2, title="🎬 Mad Max", year=2015, rating=8.5, image="AgACAgIAAxkBAAEdK9FnsbuqHVJIS4GVitbf2Nl3CEeUhQACye8xG-KdiUmkg2Zy8-X4uQEAAwIAA3kAAzYE", descr="jkhigytfrydtesrxdcfvgnjk")]


@dp.message(SectorState.movies_menu, F.text == __("🎬 Action"))
async def action_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🎬 John Wick"), _("🎬 Mad Max"), _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.action_menu)
    await message.answer("🎥 Movies Menu", reply_markup=markup)


@dp.message(SectorState.action_menu, F.text == __("🎬 John Wick"))
async def action_movie_handler(message: Message, state: FSMContext) -> None:
    first_movie = actions[0]
    image = first_movie.image
    caption = (f"{_('Name')}: {first_movie.title}\n"
               f"{_('Year')}: {first_movie.year}\n"
               f"{_('Rating')}: {first_movie.rating}\n"
               f"{_('Description')}: {first_movie.descr}"
               )
    await state.set_state(SectorState.movie_down)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)

@dp.message( F.text == __("🎬 Mad Max"),)
async def action_movie_handler(message: Message, state: FSMContext) -> None:
    second_movie = actions[1]
    image = second_movie.image
    caption = (f"{_('Name')}: {second_movie.title}\n"
               f"{_('Year')}: {second_movie.year}\n"
               f"{_('Rating')}: {second_movie.rating}\n"
               f"{_('Description')}: {second_movie.descr}"
               )
    await state.set_state(SectorState.movie_down)
    markup = pagination_inline_button()
    await message.answer_photo(image, caption=caption, reply_markup=markup)
