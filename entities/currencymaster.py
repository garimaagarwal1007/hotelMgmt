from DAO.db_util import insert
from DAO.db_conn import DAO
from flask import Blueprint

currency_master = Blueprint('currencymaster', __name__)

# class CurrencyMaster:
#     def __init__(self):
#         self.curr_name="Dollars"
#         self.curr_symbol="$"
#         self.country="USA"

@currency_master.route('/insertcurrency')
def insert_currency(obj):
         query=insert(obj)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)


##following code needs to be added into admin portal

# currency=CurrencyMaster()
# currency.curr_name="Pound"
# currency.curr_symbol="#"
# currency.country="UK"
# currency.insert_currency()