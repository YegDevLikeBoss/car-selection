class Config(object):
    DEBUG = False
    MONGO_URI = "enter your mongourl here"
    MONGODB_SETTINGS = {
        "db": "cars",
        "host": MONGO_URI,
    }
