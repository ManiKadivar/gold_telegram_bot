import asyncio
from telegram import Bot

BOT_TOKEN = '8037217846:AAELqw6m7SdseM3zJ3vIA7vIcetCwFo0bnQ'
CHAT_ID = 1168633089

bot = Bot(token=BOT_TOKEN)

async def main():
    await bot.send_message(chat_id=CHAT_ID, text="✅ پیام تستی از ربات تحلیل طلا از Render!")

asyncio.run(main())
