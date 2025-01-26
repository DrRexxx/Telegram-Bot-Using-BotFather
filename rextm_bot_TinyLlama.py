from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline

# Initialize the LLM pipeline
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device=0)

# Command Handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Rex, powered by TinyLlama. Ask me anything!")

# Handler for user messages
async def chat_with_llm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text  # Capture user input
    # Generate response using TinyLlama
    response = pipe(user_message, do_sample=True, temperature=0.5, top_k=50, top_p=0.9)[0]["generated_text"]
    await update.message.reply_text(response)

# Main function
def main():
    TOKEN = "7536444585:AAG9ZGEI3kcXP2v_uXoT4fuE8bs7nai5KPw"  # Replace with bot token

    # Creating the application
    application = Application.builder().token(TOKEN).build()

    # Adding command and message handlers
    application.add_handler(CommandHandler("start", start))  # Handles /start command
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_llm))  # Handles text messages

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
