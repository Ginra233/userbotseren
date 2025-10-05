import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "1000"))

DEVS = list(map(int, os.getenv("DEVS", "6207641651").split()))

API_ID = int(os.getenv("API_ID", "6207641651"))

API_HASH = os.getenv("API_HASH", "5a412f86203525b45a9c415670c665e8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8449681174:AAH5gYldCVl0kynboDZfkasXHJNVG_fKTr4")

OWNER_ID = int(os.getenv("OWNER_ID", "6207641651"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Gibshosting:userbotgibs333@cluster0.tistl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002499407289"))
