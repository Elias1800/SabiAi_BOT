from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# APIs
TOKEN_TELEGRAM= '7654266195:AAGYNmiIglcTHP_prxkf4VL46s3QqQLIOm0'
TOKENN_GEMINI='AIzaSyAc06fu1ntOt63CeA67hOrXpl5LDdIyWp8'

# Função que responde ao comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá, {update.effective_user.first_name}! Eu estou funcionando! 🤖")


# Inicializa o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot iniciado...")
    app.run_polling()