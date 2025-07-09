import asyncio
from telegram import Bot
from datetime import datetime, time, timedelta

BOT_TOKEN = '8037217846:AAELqw6m7SdseM3zJ3vIA7vIcetCwFo0bnQ'
CHAT_ID = 1168633089

bot = Bot(token=BOT_TOKEN)

async def send_daily_message():
    while True:
        now = datetime.now()
        target_time = datetime.combine(now.date(), time(9, 0))  # ساعت 9 صبح

        if now > target_time:
            target_time += timedelta(days=1)

        wait_seconds = (target_time - now).total_seconds()
        await asyncio.sleep(wait_seconds)

        await bot.send_message(chat_id=CHAT_ID, text="☀️ صبح بخیر! تحلیل طلای ۱۸ عیار امروز...")

async def main():
    await send_daily_message()

asyncio.run(main())
