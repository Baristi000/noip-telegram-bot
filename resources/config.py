import json
import os

class Setting:
  def __init__(self) -> None:
    file = open("./resources/mapper.json","r")
    self.data = json.load(file)
    file.close()
    
    self.bot_token = os.getenv("BOT_TOKEN","Bot-token")
        
settings = Setting()