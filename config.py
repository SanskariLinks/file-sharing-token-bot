import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26930219"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f61fa0adcd48b6bec464b6866fbd2822")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001401917601"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1809208278"))

#Port
PORT = os.environ.get("PORT", "8585")

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sobowe9677:g5NNHjWheYTsVW6P@cluster0.0mird.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#auto delete
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 1200)) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 1200)) #seconds
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
GET_AGAIN = os.environ.get("GET_AGAIN", False) #ON/OFF
DELETE_INFORM = os.environ.get("INFORM" , "Your file has been successfully deleted ✅")
NOTIFICATION = os.environ.get("NOTIFICATION" ,"This file will be automatically deleted in 20 minutes(Due to Copyright Issues).")
GET_INFORM = os.environ.get("GET_INFORM" ,"This file will be automatically deleted in 20 minutes(Due to Copyright Issues).")

BAN = int(os.environ.get("BAN", "1198543450")) #Owner user id - dont chnge 
OWNER = os.environ.get("OWNER", "BURGITY") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1809208278")) #Owner user id
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', 'BURGITY')
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "Tharki_Colony_GC") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "TharkiColony") # WITHOUR @

#Shortner (token system) 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "681754c5513b5c0801a511e9056531ebc64ade95")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 64800)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/How_T0_D0wnload/11") # shareus ka tut_vid he 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", " -1001904606496"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1480923991 5069922547 6695586027").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6376864232)

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
