from aiogram import BaseMiddleware, Bot
from aiogram.enums import ChatMemberStatus
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

Channels = [-1002335253828]


class JoinChannelMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        CHAT_IDES_LIST = [channel_id for channel_id in Channels]  # noqa
        if event.callback_query and event.callback_query.data == 'check_if_subscribed' or event.message:

            if event.message:
                user = event.message.from_user
            else:
                user = event.callback_query.from_user

            bot: Bot = data['bot']

            unsubscribers = []
            for channel_id in CHAT_IDES_LIST:
                member = await bot.get_chat_member(channel_id, user.id)
                if member.status == ChatMemberStatus.LEFT:
                    unsubscribers.append(channel_id)

            if unsubscribers:
                ikb = InlineKeyboardBuilder()
                for channel_id in unsubscribers:
                    channel = (await bot.get_chat(channel_id)).model_dump()
                    ikb.add(InlineKeyboardButton(
                        text=channel['title'],
                        url=channel['invite_link']
                    ))
                ikb.add(InlineKeyboardButton(text=_("Tekshirish✅"), callback_data="check_if_subscribed"))
                ikb.adjust(1, 1)
                if event.callback_query:
                    try:
                        await event.callback_query.message.edit_reply_markup(reply_markup=ikb.as_markup())
                    except TelegramBadRequest:
                        await event.callback_query.answer(_("Barcha kanallarga a'zo bo'ling !!!"), show_alert=True)
                else:
                    await event.message.answer(_("Oldin kanallarga a'zo bo'ling👇"), reply_markup=ikb.as_markup())
                return
            else:
                if event.callback_query:
                    await event.callback_query.message.edit_text(text="rahmat")
        return await handler(event, data)
