import Constants
from DAO import hotel_dao


class Hotels:
    def __init__(self):
        self.hotel_id = None
        self.hotel_name = None
        self.hotel_desc = None
        self.amenities = None
        self.policies = None
        self.address = None
        self.is_active = None
        self.check_in = None
        self.check_out = None

    @staticmethod
    def get_insert_hotels_header():
        return Constants.HOTEL_INSERT_HEADER

    def get_insert_hotel_values(self):
        val = f' ("{self.hotel_name}", "{self.hotel_desc}", {self.amenities},{self.policies},{self.address},{self.is_active}, "{self.check_in}", "{self.check_out}")'
        return val







