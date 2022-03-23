from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


caption = """
✍️ Logo Created Successfully✅

◇───────────────◇

🚀 **Created By** : [𝗟𝗢𝗚𝗢 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗥 🎨](https://t.me/LogoGeneraterRobot)

🌺 **Requestor** : ** {} **

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- **@AnonymousBotsInfinity**

◇───────────────◇️  
    """
#◇───────────────────────────────────────◇ 
buttons=[
    [
        InlineKeyboardButton('🍀 Update Channel 🍀', url='https://t.me/AnonymousBotsInfinity'),
        InlineKeyboardButton('🚀 Support Group 🚀', url='https://t.me/AnonymousBotsInfinitySupport'),
    ],
    [InlineKeyboardButton('🔐 Source Code 🔐', url='https://github.com/KisaraPesanjithPerera/Logo-Generater')],
]

#◇───────────────────────────────────────◇ 
START_TXT = """<b>🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮</b> {}

🙋‍♂️ 𝗜 𝗔𝗺 𝗟𝗼𝗴𝗼 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗕𝗼𝘁,𝗜 𝗖𝗮𝗻
🌺 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚎 𝙻𝚘𝚐𝚘  
🌷 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚎 𝚆𝚊𝚕𝚕𝚙𝚊𝚙𝚎𝚛
🚀 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚎 4𝚔 𝙻𝚘𝚐𝚘
🍀 𝚆𝚛𝚒𝚝𝚒𝚗𝚐 𝙾𝚗 𝙿𝚒𝚌𝚝𝚞𝚛𝚎
皿───────────────皿
🤖 𝗕𝗼𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀
࿂<code>/logo [logo name]</code>
࿂<code>/logo2 [logo name]</code>
࿂<code>/logohq [logo name]</code>
࿂<code>/write [text]</code>
࿂<code>/wall [wallpaper name]</code>

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity
#◇───────────────────────────────────────◇
PICS = (environ.get('PICS', 'https://telegra.ph/file/ab0d7d64411efca4f5076.jpg')).split()


@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_chat_action("typing")
    await message.reply(START_TXT.format(message.from_user.mention if message.from_user else message.chat.title), reply_markup=reply_markup)
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
    if len(message.command) != 2:
    reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}")
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 
  
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logohq?name={text}")
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}")
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )


logo.run()

app.start()
LOGGER.info("Anonymous Bots Infinity")
idle()
