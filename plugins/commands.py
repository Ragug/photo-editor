# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Telegram stickers",
                            url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTc2ODU0NzI4Mzk4MjY5?story_media_id=2623219158225116484_45667768285&utm_medium=share_sheet",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Report Bugs 😊",
                            url="https://www.instagram.com/ragug19?r=nametag",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Telegram stickers",
                            url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTc2ODU0NzI4Mzk4MjY5?story_media_id=2623219158225116484_45667768285&utm_medium=share_sheet",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Report Bugs 😊",
                            url="https://www.instagram.com/ragug19?r=nametag",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Telegram stickers",
                            url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTc2ODU0NzI4Mzk4MjY5?story_media_id=2623219158225116484_45667768285&utm_medium=share_sheet",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Report Bugs 😊",
                            url="https://www.instagram.com/ragug19?r=nametag",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
