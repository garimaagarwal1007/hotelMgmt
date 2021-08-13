from DAO.db_util import insert
from DAO.db_conn import DAO

class OfferDetails:
    def __init__(self):
        self.offer_desc="Paytm offer"
        self.is_percent=1
        self.offer_discount=10

    def insert_offer(self):
         query=insert(self)
         dao=DAO()
         result=dao.execute_non_execute(query)
         print(result)


##following code needs to be added into admin portal

offer=OfferDetails()
offer.offer_desc="gpay"
offer.offer_discount=500
offer.is_percent=0
offer.insert_offer()