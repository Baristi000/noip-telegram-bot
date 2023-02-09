from signal import pthread_kill, SIGKILL
from telegram.ext import ApplicationBuilder, CommandHandler
from threading import Thread
import logging

from botHandler import *
from resources.config import settings

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# Auto update every day
updater = Thread(target = update_every_day)
updater.start()


app = ApplicationBuilder().token(settings.bot_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ip", getIp))
app.add_handler(CommandHandler("info", get_all_info))
app.add_handler(CommandHandler("update", update_all))

app.run_polling()
pthread_kill(updater.ident, SIGKILL)
