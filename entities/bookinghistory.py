from flask import Blueprint,request
from DAO.db_util import insert
from DAO.db_conn import DAO

booking_history = Blueprint('bookinghistory', __name__)


# class BookingHistory:
#    def __init__(self):
#       self._booking_id=0
#       self._hotel_id=0
#       self.pmt_id=0
#       self.start_date="01/01/2000"
#       self.end_date= "01/01/2010"
#       self.room_type_id=1
#       self.rooms_count=1
#       self.guests_count=1
#       self.addons=""
#       self.booking_status=0

@booking_history.route('/createbooking')
def Create_Booking():
    data = request.data
    query = insert(data)
    dao = DAO()
    result = dao.execute_non_execute(query)
    print(result)



