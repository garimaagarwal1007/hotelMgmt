from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request

bed_type = Blueprint('bedtype', __name__)


# class RoomBedTypes:
#     def __init__(self):
#         self.bed_type_name="Single"

@bed_type.route('/insertbedtype',methods=['POST'])
def insert_bedtype():
         data= request.data
         query=insert(data)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)
