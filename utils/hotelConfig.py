import configparser

PATH = "D:\hotelMgmt\cfg\config.ini"


class Config:
    _instance = None

    @classmethod
    def get_config(cls):
        if cls._instance is None:
            cls._instance = configparser.ConfigParser()
            cls._instance.read(PATH)
        return cls._instance
