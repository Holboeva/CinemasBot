from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import I18n
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from Bot.buttons.reply import build_reply_button
from Bot.dispatcher import dp
from Bot.states import SectorState


@dp.message(SectorState.language, F.text == __("⬅️ Back"))
@dp.message(SectorState.movies_menu, F.text == __("⬅️ Back"))
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    texts = [_("🎥 Movies Menu"), _("📞 Call center"), _("🇺🇿🇷🇺🇬🇧🇫🇷 Lang")]
    markup = build_reply_button(texts, (2,))
    await message.answer(_("🏠 Main Menu:"), reply_markup=markup)


@dp.message(F.text == __("🇺🇿🇷🇺🇬🇧🇫🇷 Lang"))
async def language_menu_handler(message: Message, state: FSMContext) -> None:
    texts = _("🇺🇿 Uzbek"), _("🇷🇺 Russian"), _("🇬🇧 English"), _("🇫🇷 French"), _("⬅️ Back")
    markup = build_reply_button(texts, (4, 1))
    await state.set_state(SectorState.language)
    await message.answer(_("Choose Language: "), reply_markup=markup)


@dp.message(SectorState.language)
async def language_handler(message: Message, state: FSMContext) -> None:
    map_lang = {
        "🇺🇿 Uzbek": "uz",
        "🇷🇺 Russian": "ru",
        "🇬🇧 English": "en",
        "🇫🇷 French": "fr",
    }
    await state.clear()
    code = map_lang.get(message.text)
    await state.update_data({"locale": code})
    if hasattr(I18n, "middleware"):
        I18n.middleware.set_locale(code)
    else:
        I18n.current_locale = code
    texts = _("🎥 Movies Menu"), _("📞 Call center"), _("🇺🇿🇷🇺🇬🇧🇫🇷 Lang")
    markup = build_reply_button(texts, (2,))
    await message.answer(_("🏠 Main Menu:"), reply_markup=markup)


@dp.message(SectorState.action_menu, F.text == __("⬅️ Back"))
@dp.message(SectorState.comedy_menu, F.text == __("⬅️ Back"))
@dp.message(SectorState.drama_menu, F.text == __("⬅️ Back"))
@dp.message(SectorState.movie_down, F.text == __("⬅️ Back"))
@dp.message(F.text == __("🎥 Movies"))
async def cinema_handler(message: Message, state: FSMContext) -> None:
    texts = [_("🎭 Drama"), _("😂 Comedy"), _("🎬 Action"), _("⬅️ Back")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.movies_menu)
    await message.answer("🎥 Movies Menu:", reply_markup=markup)
