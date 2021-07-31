from utils.hotelConfig import Config
import pymysql

config = Config.get_config()


class DAO(object):
    def __init__(self, attribute="Database"):
        conn_text = config.get(attribute, 'conn_string')
        self.conn_string = conn_text.split(",")
        self.db = attribute

    def execute(self, query, conn_str=None):
        cnxn = None
        rows = []
        if conn_str is None:
            conn_str = self.conn_string
        else:
            conn_str = conn_str.split(",")
        try:
            cnxn = pymysql.connect(user=conn_str[1], passwd=conn_str[2], host=conn_str[0],
                                   database=conn_str[3], autocommit=False)
            cursor = cnxn.cursor()
            cursor.execute(query.encode('utf-8'))
            cnxn.commit()
            rows = cursor.fetchall()
        except Exception as e:
            if cnxn:
                cnxn.rollback()
            raise e
        finally:
            if cnxn:
                cnxn.close()
        return rows

    def execute_non_query(self, query, conn_str=None):
        rows = 0
        cnxn = None
        if conn_str is None:  # check connection string is provided or not
            conn_str = self.conn_string  # if connection string is not provided then use default connection string
        else:
            conn_str = conn_str.split(",")
        try:
            if query:
                cnxn = pymysql.connect(user=conn_str[1], passwd=conn_str[2], host=conn_str[0],
                                       database=conn_str[3], autocommit=False)
                cursor = cnxn.cursor()

                cursor.execute(query.encode('utf-8'))
                rows = cursor.rowcount
                cnxn.commit()
            else:
                pass
        except Exception as e:
            if cnxn:
                cnxn.rollback()
            raise e
        finally:
            if cnxn:
                cnxn.close()
        return rows
