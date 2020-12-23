import json
import pymysql

def hello(event, context):
    rds_host  = "helladb.ci1us0tjljtk.us-east-1.rds.amazonaws.com"
    name = "admin"
    password = "hellacles"
    db_name = "helladb"

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    with conn.cursor() as cur:
        cur.execute("delete from UserInfo where username='" + event['userid'] + "'")
        conn.commit()
        cur.close()

    response = {
        "statusCode": 200,
        "body": "success"
    }

    return response