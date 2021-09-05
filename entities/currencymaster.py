from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint,request

currency_master = Blueprint('currencymaster', __name__)

# class CurrencyMaster:
#     def __init__(self):
#         self.curr_name="Dollars"
#         self.curr_symbol="$"
#         self.country="USA"

@currency_master.route('/insertcurrency')
def insert_currency():
         data= request.data
         query=insert(data)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)
