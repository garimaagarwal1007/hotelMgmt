import Constants


class Hotels:
    def __init__(self, hotel_id, hotel_name, desc, amenities, policies, address, check_in='12:00 PM',
                 check_out='11:00 AM',
                 is_active=1):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_desc = desc
        self.amenities = amenities
        self.policies = policies
        self.address = address
        self.is_active = is_active
        self.check_in = check_in
        self.check_out = check_out

    @staticmethod
    def get_insert_header_for_hotel():
        return Constants.HOTEL_INSERT_HEADER

    def get_values(self):
        val = f' ("{self.hotel_name}", "{self.hotel_desc}", {self.is_active}, "{self.check_in}", "{self.check_out}")'
        return val


