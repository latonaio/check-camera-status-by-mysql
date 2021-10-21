#!/usr/bin/env python3
import MySQLdb
import simplejson as json


MYSQL_HOST = "127.0.X.X"
MYSQL_PORT = 30000
MYSQL_USER = "latona"
MYSQL_PASSWORD = "XXXXXXXX"

class UpdateDeviceStateToDB():
    def __init__(self):
        self.connection = MySQLdb.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db='PeripheralDevice',
            charset='utf8')
        self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
    
    def update_up_device_state(self):
        sql = """
            SELECT state FROM cameras
            WHERE state = 1 LIMIT 1
            """
        self.cursor.execute(sql)
        return self.cursor.fetchone()


if __name__ == "__main__":
    db = UpdateDeviceStateToDB()
    res = db.update_up_device_state()
    if isinstance(res, dict):
        try:
            print(json.dumps(res))
            exit(0)
        except Exception:
            pass
    print(json.dumps({"state": 0}))
