from telegram import Update
from telegram.ext import ContextTypes
import logging

from noip import get_ip, update_ip_domain
from resources.config import settings
import time


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(f'Hello {update.effective_user.first_name} {update.effective_user.last_name}')
    
async def getIp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  ip = get_ip()
  logging.info(f"Current ip: {str(ip)}")
  await update.message.reply_text(f"Current ip: {str(ip)}")
  
async def get_all_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  result = ""
  for item in settings.data:
    result += "\ndomain:\t" + item["domain"] + "\nusername:\t" + item["username"]+ "\npassword:\t" + item["password"] + "\n---"
  logging.info(result)
  await update.message.reply_text(result)

async def update_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  ip = get_ip()
  message = ""
  for item in settings.data:
    domain = item["domain"]
    update_status = update_ip_domain(
      item["username"],
      item["password"],
      domain,
      ip
    )
    if update_status == 200:
      message += f'Map succeed:\nip:{str(ip)}\ndomain: {domain}\n---\n'
      logging.info(f'Map succeed ip:{str(ip)} to {domain}')
    else:
      message += f'Map false\nip: {str(ip)}\ndomain: {domain}\n---\n'
      logging.warning(f'Map false ip:{str(ip)} to {domain}')
  await update.message.reply_text(message)

def update_every_day():
  while True:
    logging.info("Starting update every day:")
    ip = get_ip()
    for item in settings.data:
      domain = item["domain"]
      update_status = update_ip_domain(
        item["username"],
        item["password"],
        domain,
        ip
      )
      if update_status == 200:
        logging.info(f'Map succeed ip:{str(ip)} to {domain}')
      else:
        logging.warning(f'Map false ip:{str(ip)} to {domain}')
    time.sleep(3600*24)
  logging.info("Bot is down, update evrey day is down")

def test():
  logging.info("Cront is running")