import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

# 🔧 লগ কনফিগার
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ Start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি AI OCR বট। তুমি কি করতে চাও? 📷 ছবি থেকে লেখা পড়া, ✅ ঠিকঠাক করা, 📄 ফাইল বানানো?")

# 📩 সব মেসেজ ধরার হ্যান্ডলার (পরবর্তীতে কাস্টমাইজ করব)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 তুমি কিছু পাঠিয়েছো। এখন আমি কী করবো সেটা বলো — যেমন: ছবি পড়বো, লেখার ভুল ঠিক করবো, নাকি ফাইল বানাবো?")

# 🤖 অ্যাপ রান
if __name__ == '__main__':
    TOKEN = os.getenv("7871717451:AAFgWQZt0yiiDKfGcW9D3j_IGaOSomjvLGE")  # 🛡️ নিরাপদভাবে টোকেন রাখার জন্য

    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("🤖 বট চালু হচ্ছে...")
    app.run_polling()