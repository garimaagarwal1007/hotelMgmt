import Constants

class HotelRooms:

    def __init__(self, hotel_room_id, room_type_id, hotel_id, room_no, room_desc, bed_type, is_air_conditioned):
        self.hotel_room_id = hotel_room_id
        self.room_type_id = room_type_id
        self.hotel_id = hotel_id
        self.room_no = room_no
        self.room_desc = room_desc
        self.bed_type = bed_type
        self.is_air_conditioned = is_air_conditioned

    @staticmethod
    def get_insert_header():
        return Constants.HOTEL_ROOMS_INSERT_HEADER

    def get_values(self):
        value = f'("{self.room_type_id}","{self.hotel_id}", "{self.room_no}", "{self.room_desc}", "{self.bed_type}", "{self.is_air_conditioned}")'
        return value


# test1 = []
# test = HotelRooms(1, 1, 1, 'A101', 'test desc', 'single bed', 1)
# test1.append(test)
# print(test.get_insert_header() + test.get_values())
