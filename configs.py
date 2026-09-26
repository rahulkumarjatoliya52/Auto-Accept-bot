from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "33728008"))
    API_HASH = getenv("API_HASH", "ee5cb6ceee9850b8521b1f80d59eade2")
    BOT_TOKEN = getenv("BOT_TOKEN", "8919266977:AAGjyZqhE0tDvbbGFBemB99H0wYCpjPX0k0")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1004487124713")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "8910598742").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jack935243:Rahul8107@cluster0.k2lf3c8.mongodb.net/?appName=Cluster0")
    
cfg = Config()
