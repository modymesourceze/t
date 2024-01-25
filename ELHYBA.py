import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from mody import Mody
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
import sqlite3
import re
from requests import *
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus  

Elhyba = Client(
   "Telegraph Uploader",
   api_id=Mody.API_ID,
   api_hash=Mody.API_HASH,
   bot_token=Mody.ELHYBA,
)

@Elhyba.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Elhyba.send_message(
               chat_id=message.chat.id,
               text="""<b>اهلا {message.from_user.mention},
🔮أنا هنا لإنشاء روابط التلجراف لملفات الوسائط الخاصة بك.

👨🏼‍💻ما عليك سوى إرسال ملف وسائط صالح مباشرة إلى هذه الدردشة.
♻️انواع الملفات الصالحه هي:- 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

🌐لأنشاء الروابط في المجموعات,اضفني لمجموعه خارقه اي عامه وارسل الامر <code>/tl</code> ردا علي ملف وسائط صالح.
🖥 | [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱](https://t.me/Source_Ze)

☣️ | [⧛𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮](https://t.me/ELHYBA)</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "↯ للمساعده ↯", callback_data="help"),
                                        InlineKeyboardButton(
                                            "↯ قناة المطور ↯", url="https://t.me/Source_Ze"),
                                         InlineKeyboardButton(

                                            "↯ قناة الملفات ↯", url="https://t.me/UP_UO")
                                    ]]
                            ),
            disable_web_page_preview=True,        
            parse_mode="html")

@Elhyba.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Elhyba.send_message(
               chat_id=message.chat.id,
               text="""<b>مرحبا صديقي انا بوت تلجراف ميديا 

👻 هذا هو بوت استخراج رابط تليجراف ميديا الخاص في ســورس زد إي اختر ماتريد من الاسفل 
👇 تسطيع استخراج 👇

📽️ فيديوهات قصيره (ان لايتعدا حجمه 5MB).
🎬 فيديوهات مرحليه.
🖼️ صورة.
💥 متحركة.
💟 ملصق.
📜 ملفات نصيه.
📩 صندوق دعم.
👥 مجموعة الدعم.
🚀 الاستخراج السريع .

✍️هذا هو بوت استخراج رابط تلجراف ميديا الخاص بــســورس زد إي 
ارسل لي اي شئ تريده لاجعله رابط ්😝

اذا احتجت اي مساعدة راسل المطور @elhyba</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙رجوع", callback_data="start"),
                                        InlineKeyboardButton(
                                            "👻حول", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Elhyba.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Elhyba.send_message(
               chat_id=message.chat.id,
               text="""<b>حول هذا البوت!</b>

<b>☘️ المبرمج :</b> <a href="https://t.me/elhyba">FORM Egypt🇪🇬</a>

<b>🔆اللغة:</b> <a href="https://www.python.org/">Python 3</a>

<b>♻️اصدار بايروجرام 1.4.16:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@Source_Ze</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙رجوع", callback_data="help"),
                                        InlineKeyboardButton(
                                            "❌اغلاق", callback_data="close")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Elhyba.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("جاري استخراج الرابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("ارسل صوره حجمها اقل من 5mb!") 
    else:
        await msg.edit_text(f'**تم استخراج رابط تليجراف ميديا بنجاح!\n\n👻https://graph.org{response[0]}\n\nJoin @Source_Ze**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Elhyba.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("جاري استخراج الرابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم الفيديو القصير يجب ان يكون اقل من 5mb!") 
    else:
        await msg.edit_text(f'**تم رفع الملف الخاص بك إلى تليجراف بنجاح!\n\n👻https://graph.org{response[0]}\n\nJoin @Source_Ze**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Elhyba.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("جار رفع إلى تليجراف...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**تم استخراج رابط تلجراف ميديا بنجاح!\n\n👻https://graph.org{response[0]}\n\nJoin @Source_Ze**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Elhyba.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
        
@Elhyba.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("🔮انتظر قليلا...")
        async def progress(current, total):
            await text.edit_text(f"📥 جاري التنزيل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 جاري الرفع الي التليجراف...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"🌐 | رابط التليجراف:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"❌ | فشل رفع الملف\n\n<i>Reason: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                            

print(
    """
Bot Started!
Join @Source_Ze
"""
)

Elhyba.run()
