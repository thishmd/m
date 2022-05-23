import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("لحضه..")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>-›  بنك</b> `{delta_ping * 1000:.3f} ms` \n<b>-›  وقت</b> - `{uptime}`"
    )


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تح"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("اني")
    await loli.edit("احبك")
    await loli.edit("@")
    await loli.edit("انتضر")
    await loli.edit("هسه")
    await loli.edit("شويه")
    await loli.edit("او")
    await loli.edit("يحدث")
    await loli.edit("@")
    await loli.edit("خلاص اشتغل")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b> 𝖍𝖎 メ  {m.from_user.mention}.

**حط نقطه ويه الاوامر**

**للتشغيل** :
**تشغيل اغنيه** ← : [ ` {HNDLR} شغل` ] رد عله الملف لو تحط أسم الاغنيه .
**تشغيل مقطع** ← : [ `‏{HNDLR}شغل_فيد` ] رد عله المقطع لو تحط اسمه .

**اللتحميل** : 
**تحمل اغنيه** ← : [ `‏{HNDLR}بحث` ] لو رابط لو اسم الاغنيه .
**تحمل مقطع** ← : [ `‏{HNDLR}بحث_فيد` ] كذالك لو رابط لو…

**تسكته** :
**تسكت البوت** ← : [ `‏{HNDLR}اسكت` او `‏{HNDLR}اوكف` ] .

**تتخطى** :
**تتخطى الاغنيه** ← : [ `‏{HNDLR}ت` ] .

 **قناة البوت اشترك بيها حته تعرف البوت من يوكف او تحديثات عن الاوامر** .

The Channel : @kzzgg 
"""
    await m.reply(HELP)
@Client.on_message(filters.command(["المطور"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""hi {m.from_user.mention}.

The Music Userbot
 The developer : @thishmd 
"""
    await m.reply(REPO, disable_web_page_preview=True)
