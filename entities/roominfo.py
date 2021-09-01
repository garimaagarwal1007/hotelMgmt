from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request

room_info = Blueprint('roominfo', __name__)
# class RoomInfo:
#     def __init__(self):
#         self.hotel_id=1
#         self.room_type_id=1
#         self.room_no=101
#         self.room_desc="fully furnished room"
#         self.bed_type=1
#         self.is_air_conditioned=1

@room_info.route('/insertroominfo',methods=['POST'])
def insert_roominfo():
         data= request.data
         query=insert(data)
         dao=DAO()
         print(query)
         result=dao.execute_non_execute(query)
         print(result)


##following code needs to be added into admin portal

# room_info=RoomInfo()
# room_info.insert_roominfo()