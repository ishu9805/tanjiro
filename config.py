import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = "7237373931:AAE9FxfrS_YYmxZJUkI9JnK41RDtVYODrdE"
API_ID = 28122413
API_HASH = "750432c8e1b221f91fd2c93a92710093"


OWNER_ID = 5803814257
DB_URL = "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = -1001975521991
FORCE_SUB_CHANNEL = -1002207066555
FORCE_SUB_CHANNEL2 = -1002199281361
FORCE_SUB_CHANNEL3 = -1002098033314
FORCE_SUB_CHANNEL4= -1002231734064


FILE_AUTO_DELETE = 600 # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = 4



try:
    ADMINS=[7453770651]
    for x in (os.environ.get("ADMINS", "7453770651").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(7453770651)

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
