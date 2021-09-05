from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request

room_type_info = Blueprint('roomtypeinfo', __name__)


# class RoomTypeInfo:
#     def __init__(self):
#         self.room_type_name="Classic"
#         self.room_size="450sq.ft"
#         self.refundable=1
#         self.actual_price=2500
#         self.display_price=2000

@room_type_info.route('/insertroomtype',methods=['POST'])
def insert_room_type():
    print("hello world")
    data = request.data
    query=insert(data)
    dao=DAO()
    result=dao.execute_non_execute(query)
    print(result)
