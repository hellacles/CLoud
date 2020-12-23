import json
import pymysql

def hello(event, context):
    rds_host  = "helladb.ci1us0tjljtk.us-east-1.rds.amazonaws.com"
    name = "admin"
    password = "hellacles"
    db_name = "helladb"

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    with conn.cursor() as cur:
        cur.execute(" SELECT *, (6371*acos(cos(radians("+event['lat']+"))*cos(radians(fromLatitude))*cos(radians(fromLongitude)-radians("+event['long']+"))+sin(radians("+event['lat']+"))*sin(radians(fromLatitude)))) AS distance FROM DeliveryInfo where userName is null and status = 0 HAVING distance <= 1 ORDER BY distance LIMIT 1 ")
        conn.commit()
        cur.close()
        result = cur.fetchone()

        print(result)

    response = {
        "statusCode": 200,
        "body": result
    }

    return response
