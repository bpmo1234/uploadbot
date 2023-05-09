#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "5695817871:AAEh9NCg1bt0NuOp_XZKARRkmCppf8EEQP0") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "20801339")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "8af2b8a51f7bdadc95641f5986cdc160") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", bpmo1996)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "") # Get from MongoDB Atlas

