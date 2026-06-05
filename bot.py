from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Анализ Авито.\n\n"
        "Команды:\n"
        "/start\n"
        "/help\n"
        "/analyze"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Пока доступна тестовая версия бота."
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Модуль анализа Авито скоро будет подключен."
    )

def main():
    import os

    token = os.getenv("BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("analyze", analyze))

    app.run_polling()

if __name__ == "__main__":
    main()
