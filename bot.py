from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Reemplaza con tu token
TOKEN = "7827290034:AAFtSzBTAGrHoK_furou0UHAncf8ma1-ptE"


# Lista de respuestas aleatorias
RESPUESTAS = [
    "¡Eso suena interesante!",
    "Cuéntame más sobre eso.",
    "Jaja, buena esa. 😂",
    "No estoy seguro de qué decir, pero suena genial.",
    "¡Me gusta cómo piensas!"
]

# Función para el comando /start
async def start(update: Update, context):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram. 😊")

# Función para responder mensajes de texto
async def responder(update: Update, context):
    texto = update.message.text.lower()

    if "hola" in texto:
        respuesta = "¡Hola! ¿Cómo estás?"
    elif "cómo estás" in texto:
        respuesta = "¡Estoy bien! Aunque técnicamente, soy solo código. 😆"
    elif "adiós" in texto:
        respuesta = "Nos vemos pronto. 👋"
    else:
        respuesta = random.choice(RESPUESTAS)

    await update.message.reply_text(respuesta)

# Función para el comando /info
async def info(update: Update, context):
    await update.message.reply_text("Soy un bot en desarrollo creado por Omega. 🚀")

# Función principal para ejecutar el bot
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Agregar manejadores de comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    
    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
