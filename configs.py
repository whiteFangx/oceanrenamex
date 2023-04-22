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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5974140023:AAF7GLJUb9lg2fNoz7oadiP1DcIGuhE6Hx4")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1476517140))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "5743243857 5751548638 1476517140 1928568176 5858467322 1827695840 1172340595 1858995207 6011680633 5347606696 1711005257 1694138821 1245624597 1380685014 917790252").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ok:ok@cluster0.ox6obby.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001745287248"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
