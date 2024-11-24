from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "22725285"))
    API_HASH = getenv("API_HASH", "f07c8bb1095ff72371e7d9c4655b4994")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "6264941380:AAGgAVj9IUAve4R9S7dr_e7k5x0xwlXpR2Y")
    OWNER_ID = int(getenv("OWNER_ID", "6213690669"))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "MehHridoy")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "MehHridoy")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1001804048226"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://itsmehhridoy:56ctjKCdvmWLSrnn@cluster0.amhq7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    DB_NAME = getenv("DB_NAME", "ExonRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
