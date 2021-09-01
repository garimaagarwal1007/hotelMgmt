from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint

bed_type = Blueprint('bedtype', __name__)


# class RoomBedTypes:
#     def __init__(self):
#         self.bed_type_name="Single"

@bed_type.route('/insertbedtype',methods=['POST'])
def insert_bedtype(obj):
         query=insert(obj)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)


##following code needs to be added into admin portal

# bed_type=RoomBedTypes()
# bed_type.insert_bedtype()