import os

DEVS = [
    940232666
]
API_ID = int(os.getenv("API_ID", "26724473"))

API_HASH = os.getenv("API_HASH", "7bc7d1f9b2f3d3f1bfd272db56ac0ba1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", "940232666"))

USER_ID = list(map(int,os.getenv("USER_ID", "940232666",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002009684047"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002119660672").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

COMMAND = os.getenv("COMMAND", ".")

OPENAI_KEY = os.getenv("OPENAI_KEY")

SUDO_USER = os.getenv("SUDO_USER", "940232666")

PREFIX = COMMAND.split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
