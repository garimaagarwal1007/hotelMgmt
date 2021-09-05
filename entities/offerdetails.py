from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request

offer_details = Blueprint('offerdetails', __name__)

# class OfferDetails:
#     def __init__(self):
#         self.offer_desc="Paytm offer"
#         self.is_percent=1
#         self.offer_discount=10

@offer_details.route('/insertoffer',methods=['POST'])
def insert_offer():
         data = request.data
         query=insert(data)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)

