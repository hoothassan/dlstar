import os 

class Config:

    class config:
        APP_ID = 50000

        API_HASH = "21ab7cb0a453b5e68986dc7bbeb701cb"
        
        BOT_TOKEN = "1215711283:AAGssccgzXz4WSR9evGBWqZIiJiW0nSmcug"
        
        STATS_CHANNEL = -1001249461809

        HOST = "127.0.0.1"

        PORT = os.getenv('PORT')

        ROOT_URI = f"http://dlgram.ml"

        ENCODING = "utf8"


        # ALLOWED_EXT = ["mkv", "mp4", "flv"]
