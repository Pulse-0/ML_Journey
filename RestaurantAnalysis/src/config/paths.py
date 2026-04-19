import os

BASE_PATH = os.path.dirname(os.path.filename(os.path.dirname(__file__)))
RAW_DATA_PATH = os.path.join(BASE_PATH,"data","raw","HyderabadRestaurants.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_PATH,"data","processed","cleaned.csv")
