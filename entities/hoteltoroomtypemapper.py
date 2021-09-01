from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint

hotel_roomtype_mapper = Blueprint('hoteltorromtypemapper', __name__)

# class HotelToRoomTypeMapper:
#     def __init__(self):
#         self.hotel_id=1
#         self.room_type_id=1


@hotel_roomtype_mapper.route('/insertroomtype')
def insert_mapper(self):
         query=insert(self)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)


# ##following code needs to be added into admin portal
#
# htrt=HotelToRoomTypeMapper()
#
# htrt.insert_mapper()