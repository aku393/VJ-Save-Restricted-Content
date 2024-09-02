import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7246880320:AAGPRcq_9Lr6x68Ytw1npiCVXthgVZjLg7w")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20176556"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8136bd26f62a889221fc6d25cebe4e6a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akuspart:xswhARGUtukiR4bK@cluster0.dmxsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
