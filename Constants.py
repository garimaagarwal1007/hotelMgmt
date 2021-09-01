HOTEL_INSERT_HEADER = """insert into Hotel (hotel_name, hotel_desc, is_active, check_in, check_out) values"""

HOTEL_ROOMS_INSERT_HEADER = """insert into hotel_rooms (room_type_id, hotel_id, room_no, room_desc, bed_type, is_air_conditioned) values"""

ROOM_TYPE_INSERT_HEADER = """insert into room_type (room_type_name, room_area, room_count, actual_price, display_price, is_active) values"""

ROOM_SERVICES_INSERT_HEADER = """insert into room_services (service_name, price, is_active) values"""

ROOM_TYPE_MAP_ROOM_SERVICES_INSERT_HEADER = """insert into room_type_map_room_services (room_type_id, room_service_id, is_active) values"""
