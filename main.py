import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from ai.brain import process_ai

TOKEN = os.getenv("BOT_TOKEN")

async def ia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    text = " ".join(context.args)

    if not text:
        await update.message.reply_text(
            "Use:\n/ia <mensagem>\n\nEx: /ia recomenda algo dark"
        )
        return

    reply, cover = await process_ai(user_id, text)

    if cover:
        await update.message.reply_photo(cover, caption=reply)
    else:
        await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("ia", ia_command))

app.run_polling()
