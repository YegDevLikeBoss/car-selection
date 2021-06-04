class Config(object):
    DEBUG = False
    MONGO_URI = "mongodb+srv://neo:antic@cool-story-bro-sewzg.mongodb.net/cars?retryWrites=true&w=majority"
    MONGODB_SETTINGS = {
        "db": "cars",
        "host": MONGO_URI,
    }