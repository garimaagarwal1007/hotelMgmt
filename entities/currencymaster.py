from DAO.db_util import insert
from DAO.db_conn import DAO

class CurrencyMaster:
    def __init__(self):
        self.curr_name="Dollars"
        self.curr_symbol="$"
        self.country="USA"

    def insert_currency(self):
         query=insert(self)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)


##following code needs to be added into admin portal

currency=CurrencyMaster()
currency.curr_name="Pound"
currency.curr_symbol="#"
currency.country="UK"
currency.insert_currency()