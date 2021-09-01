from flask import Blueprint

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


   @property
   def booking_id(self):
      return self._booking_id

   # @booking_id.setter
   # def booking_id(self,id):
   #     self._booking_id=id

   @property
   def hotel_id(self):
       return self._hotel_id

   # @hotel_id.setter
   # def hotel_id(self,id):
   #     self._hotel_id=id

   @property
   def pmt_id(self):
       return self._pmt_id

   @pmt_id.setter
   def pmt_id(self,id):
       self._pmt_id=id

   @property
   def start_date(self):
       return self._start_date

   @start_date.setter
   def start_date(self, date):
       self._start_date = date

   @property
   def end_date(self):
       return self._end_date

   @end_date.setter
   def end_date(self, date):
       self._end_date = date

   @property
   def room_type_id(self):
       return self._room_type_id

   @room_type_id.setter
   def room_type_id(self, type_id):
       self._room_type_id = type_id

   @property
   def rooms_count(self):
      return self._rooms_count

   @rooms_count.setter
   def rooms_count(self, count):
       self._rooms_count = count

   @property
   def guests_count(self):
      return self._guests_count

   @guests_count.setter
   def guests_count(self, count):
       self._guests_count = count

   @property
   def addons(self):
      return self._addons

   @addons.setter
   def addons(self,addons):
       self._addons = addons

   @property
   def booking_status(self):
      return self._booking_status

   @booking_status.setter
   def booking_status(self, booking_status):
       self._booking_status = booking_status

   @property
   def customer_id(self):
      return self._customer_id

   @customer_id.setter
   def customer_id(self, cust_id):
       self._customer_id = cust_id

   @property
   def created_date(self):
      return self._created_date

   @created_date.setter
   def created_date(self, date):
       self._created_date = date

   @property
   def updated_date(self):
      return self._updated_date

   @updated_date.setter
   def updated_date(self, date):
       self._updated_date = date

   @property
   def booking_source(self):
      return self._booking_source

   @booking_source.setter
   def booking_source(self, source):
       self._booking_source = source

   @property
   def offer_id(self):
      return self._offer_id

   @offer_id.setter
   def offer_id(self, id):
       self._offer_id = id

   @property
   def cancellation_reason(self):
      return self._cancellation_reason

   @cancellation_reason.setter
   def cancellation_reason(self, reason):
       self._cancellation_reason = reason

   @property
   def refund_amount(self):
      return self._refund_amount

   @refund_amount.setter
   def refund_amount(self, amount):
       self._refund_amount = amount

# grad_obj = BookingHistory(123,1)
# #grad_obj.booking_id=123
# print(grad_obj.booking_id)
# # grad_obj.hotel_id=1
# print(grad_obj.hotel_id)
# #grad_obj.Aboutyear = 2018
# #print(grad_obj.Aboutyear)
#
# def create_structure():


