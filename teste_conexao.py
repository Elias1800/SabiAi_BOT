from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# APIs
TOKEN_TELEGRAM= ''
TOKENN_GEMINI=''

# Função que responde ao comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá, {update.effective_user.first_name}! Eu estou funcionando! 🤖")

async def Eu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Teste")


# Inicializa o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("Eu", Eu))

    print("Bot iniciado...")
    app.run_polling()