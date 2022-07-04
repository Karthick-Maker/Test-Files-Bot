import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
#TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
TG_BOT_TOKEN = "5588177593:AAGwl2Ot_ChKNzyHRzEXRSM7VgUCnlKevCc"

#Your API ID from my.telegram.org
#APP_ID = int(os.environ.get("APP_ID", ""))
APP_ID = int("12610835")

#Your API Hash from my.telegram.org
#API_HASH = os.environ.get("API_HASH", "")
API_HASH = "886233f38d7d06f369974fddb7842f36"

#Your db channel Id
#CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
CHANNEL_ID = int("-1001485941401")

#OWNER ID
#OWNER_ID = int(os.environ.get("OWNER_ID", ""))
OWNER_ID = int("5398449311")

#Database 
#DB_URI = os.environ.get("DATABASE_URL", "")
#DB_URI = ""

#force sub channel id, if you want enable force sub
#FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL = int("0")

#TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
TG_BOT_WORKERS = int("4")
#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1192254405)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
