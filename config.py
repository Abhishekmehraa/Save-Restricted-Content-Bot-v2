# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "18056075"))
API_HASH = getenv("API_HASH", "b21ad82be8e005dd61a5421b7e4c9864")
BOT_TOKEN = getenv("BOT_TOKEN", "8162646860:AAHRBgzvYv485GsYobNsdU9seUt4uKsWbmg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7569345648").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ajaysaranmongo:CNoCTyosIJuet2U3@cluster0.rieo5qs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002873700697")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002843573290"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
