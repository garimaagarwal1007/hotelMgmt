import Constants
from DAO import hotel_dao
from DAO.db_util import insert, read,delete


class Hotels:
        @property
        def hotel_id(self):
                return self._hotel_id

        @hotel_id.setter
        def hotel_id(self,hotel_id):
                self._hotel_id=hotel_id

        @property
        def hotel_name(self):
                return self._hotel_name

        @hotel_name.setter
        def hotel_name(self,hotel_name):
                self._hotel_name=hotel_name

        @property
        def hotel_desc(self):
            return self._hotel_desc

        @hotel_desc.setter
        def hotel_desc(self, hotel_desc):
            self._hotel_desc = hotel_desc

        @property
        def amenities(self):
            return self._amenities

        @amenities.setter
        def amenities(self, amenities):
            self._amenities = amenities

        @property
        def policies(self):
            return self._policies

        @policies.setter
        def policies(self, policies):
            self._policies = policies

        @property
        def address(self):
            return self._address

        @address.setter
        def address(self, address):
            self._address = address

        @property
        def is_active(self):
            return self._is_active

        @is_active.setter
        def is_active(self, is_active):
            self._is_active = is_active

        @property
        def check_in(self):
            return self._check_in

        @check_in.setter
        def check_in(self, check_in):
            self._check_in = check_in

        @property
        def check_out(self):
            return self._check_out

        @check_out.setter
        def check_out(self, check_out):
            self._check_out = check_out



hotel = Hotels()
hotel.hotel_id=4
hotel.hotel_name='Taj avenue'
hotel.is_active=1
hotel.address='near airoli'
hotel.amenities='spacious'
hotel.check_in='11:00 am'
hotel.check_out='12:00 pm'
print(insert(hotel))
print(read(hotel))
print(delete(hotel))


