from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from entities.RoomTypeInfo import room_type_info
from entities.bedtype import bed_type
from entities.roominfo import room_info
from entities.offerdetails import offer_details
from entities.currencymaster import currency_master
from entities.hoteltoroomtypemapper import hotel_roomtype_mapper

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

app.register_blueprint(room_type_info)
app.register_blueprint(bed_type)
app.register_blueprint(room_info)
app.register_blueprint(offer_details)
app.register_blueprint(currency_master)
app.register_blueprint(hotel_roomtype_mapper)

@app.route('/')
def home():
    return "hello";


if __name__ == '__main__':
    app.run(debug=True)