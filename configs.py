import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 10683462))
    API_HASH = os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5680348811:AAFTg0TmzNx6dBPG5A2TQ3meJq3_npGVs2A")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQBbv3ZEDjihY4mXoFdZTyr9OqFeTqEaDqBYqby8x9HVYpSx0y8U18FiEbDIK73PnjEJdNEzy_cueymotgCEWBSdVmd8iIv7tShqQyve-wREJIEub9nUQwk9w8izL_nUC-Okaa_ljGzYV7hieMUFbCA5M6E_Ml4HTkvAo2pqsOolFBzzPbgg1booF24oAtUR0kvNNuWai6iUGOoGtp3xpT-IUC8z--JbH7M5xHpPCQ716Xf6Em85kTYkg6Im9OtjQOCoLZhua8U8cw9npu_2iIUq43Wb7oBr6ieiAvX7KahUZwDoUvnANhPtyFTaE-E2g_gnif60W_1l4yRhjso9IHN7AAAAAVLdr70A")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001838491668"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "greymatters_test_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5685227453"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "udhdin")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

