from utils.hotelConfig import Config
import pymysql

config = Config.get_config()


class DAO:
    def __init__(self, attribute="Database"):
        conn_text = config.get(attribute, 'conn_string')
        self.conn_string = conn_text.split(",")
        self.db = attribute

    def execute(self, query, conn_str=None):
        cnxn = None
        rows = []
        if conn_str is None:
            conn_str = self.conn_string
        try:
            cnxn = pymysql.connect(user=conn_str[1], passwd=conn_str[2], host=conn_str[0],
                                   database=conn_str[3], autocommit=False)
            cursor = cnxn.cursor()
            cursor.execute(query.encode('utf-8'))
            rows = cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cnxn:
                cnxn.close()
        return rows
