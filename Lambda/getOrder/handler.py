import json
import pymysql

def hello(event, context):
    rds_host  = "helladb.ci1us0tjljtk.us-east-1.rds.amazonaws.com"
    name = "admin"
    password = "hellacles"
    db_name = "helladb"
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    with conn.cursor() as cur:
        cur.execute("select shopName, fromAddress, destination \
            from DeliveryInfo where userName is null and status=0 LIMIT 1;")
        conn.commit()
        cur.close()
        status = cur.fetchone()
        shopName = status[0]
        shopAddress = status[1]
        destination = status[2]

    response = {
        "statusCode": 200,
        "shopName": shopName,
        "shopAddress": shopAddress,
        "destination": destination
    }

    return response
