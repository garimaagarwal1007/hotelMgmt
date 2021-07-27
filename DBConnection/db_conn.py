import pymongo
from pymongo import MongoClient

from utils.hotelConfig import Config

CONFIG = Config.get_config()
# for sect in CONFIG.sections():
#     for k, v in CONFIG.items(sect):
#         print(k, v)


print(CONFIG.get('DB', 'conn_string'))
conn_str = CONFIG.get('DB', 'conn_string')

client = MongoClient(conn_str)
db_name = client["HotelMgmt"]
collection_name = db_name["hotels"]

all_item_details = collection_name.find()
for item in all_item_details:
    #     # This does not give a very readable output
    print(item)

