import Constants

class RoomType:

    def __init__(self, room_type_id, room_type_name, room_area, room_count, actual_price, display_price, room_type_is_active, room_service_id, room_service_name, room_service_price, room_service_is_active, room_type_map_room_services_id, room_type_map_room_services_is_active):
        self.room_type_id = room_type_id
        self.room_type_name = room_type_name
        self.room_area = room_area
        self.room_count = room_count
        self.actual_price = actual_price
        self.display_price = display_price
        self.room_type_is_active = room_type_is_active
        self.room_service_id = room_service_id
        self.room_service_name = room_service_name
        self.room_service_price = room_service_price
        self.room_service_is_active = room_service_is_active
        self.room_type_map_room_services_id = room_type_map_room_services_id
        self.room_type_map_room_services_is_active = room_type_map_room_services_is_active

    @staticmethod
    def get_room_type_insert_header():
        return Constants.ROOM_TYPE_INSERT_HEADER

    @staticmethod
    def get_room_service_insert_header():
        return Constants.ROOM_SERVICES_INSERT_HEADER

    @staticmethod
    def get_room_type_map_room_services_insert_header():
        return Constants.ROOM_TYPE_MAP_ROOM_SERVICES_INSERT_HEADER

    def get_room_type_values(self):
        value= f'("{self.room_type_name}", "{self.room_area}", "{self.room_count}", "{self.actual_price}", "{self.display_price}", "{self.room_service_is_active}")'
        return value

    def get_room_services_value(self):
        value= f'("{self.room_service_name}", "{self.room_service_price}", "{self.room_service_is_active}")'
        return value

    def get_room_type_map_room_services_value(self):
        value= f'("{self.room_type_id}", "{self.room_service_id}", "{self.room_type_map_room_services_is_active}")'
        return value

# test1 = []
# test = RoomType(1, 'deluxe', '350 sqft', '5', '1500', '2000', 1, 1, 'with a view', '200', 1, 1, 1)
# test1.append(test)
# print(test.get_room_type_insert_header() + test.get_room_type_values())
# print(test.get_room_service_insert_header() + test.get_room_services_value())
# print(test.get_room_type_map_room_services_insert_header() + test.get_room_type_map_room_services_value())