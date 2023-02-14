# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "4783634"))
    API_HASH = os.environ.get("API_HASH", "f6c33f46599246676f75e153b615dbbc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6092663926:AAE124kuVPUZclLVZjiCT4-41O6ghIyrgPw")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1476517140))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1277025786").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ok:ok@cluster0.ox6obby.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001745287248"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
