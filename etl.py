# -*- coding: utf-8 -*-

import connection as conn
import pandas as pd
import pyodbc 
import json


def etl():
    cnxn = conn.sqlConnect()
    cursor = cnxn.cursor()

    # Truncate tables 
    cursor.execute('''delete from NYCTAXI.TRIP;''')
    cursor.execute('''delete from NYCTAXI.VENDOR;''')
    cursor.commit()

    # Load the VENDOR table from blob storage
    dfVendor = pd.read_csv('https://generalfile.blob.core.windows.net/file-storage/data-vendor_lookup-csv.csv?sp=r&st=2020-08-16T17:59:45Z&se=2020-11-01T01:59:45Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=0u6oPfgGpdtvh3Smsp9I6JB1iYnq5nk0VHPoRPuE4Xs%3D')
    
    for row in dfVendor.itertuples():
        cursor.execute('''insert into NYCTAXI.VENDOR(VENDOR_ID, NAME, ADDRESS, CITY, STATE, ZIP, COUNTRY, CONTACT, CURRENT_FLAG) values(?, ?, ?, ?, ?, ?, ?, ?, ?);''', 
                       row.vendor_id, row.name, row.address, row.city, row.state, row.zip, row.country, row.contact, row.current)
    
    # Commit the inserts on VENDOR table
    cursor.commit()

    #Load the TRIP table from blob storage
    source = ['https://generalfile.blob.core.windows.net/file-storage/data-sample_data-nyctaxi-trips-2009-json_corrigido.json?sp=r&st=2020-08-16T18:00:43Z&se=2020-11-01T02:00:43Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=tyClzriwCa9st%2FLk2fM0l%2BQ%2F7nb5%2BKmzl7MADrqYFrc%3D'#,
              'https://generalfile.blob.core.windows.net/file-storage/data-sample_data-nyctaxi-trips-2010-json_corrigido.json?sp=r&st=2020-08-16T18:01:27Z&se=2020-11-01T02:01:27Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=VA5OzvNfatipB9RPOlagS5C6YN6yybanHNXtn1D5w2I%3D',
              'https://generalfile.blob.core.windows.net/file-storage/data-sample_data-nyctaxi-trips-2011-json_corrigido.json?sp=r&st=2020-08-16T18:01:57Z&se=2020-11-01T02:01:57Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=x1FGv8HK1tB3Qq%2FZ%2BRTlyMN%2FpZSN0NpnYnttbPxUNqE%3D',
              'https://generalfile.blob.core.windows.net/file-storage/data-sample_data-nyctaxi-trips-2012-json_corrigido.json?sp=r&st=2020-08-16T18:02:34Z&se=2020-11-01T02:02:34Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=4E%2ByunIB39pJFQp%2Fd64jbxWsOWJRFIHjZYAGRoiWRzI%3D'
             ]
    dfTrip = pd.DataFrame()
    
    for s in source:
        dfTrip = dfTrip.append(pd.read_json(s, lines=True))
    
    dfTrip = dfTrip.fillna(value=0)

    # Create a lookup list to the payment_type column
    dfPayment = pd.read_csv('https://generalfile.blob.core.windows.net/file-storage/data-payment_lookup-csv.csv?sp=r&st=2020-08-16T21:25:41Z&se=2020-10-31T05:25:41Z&sip=0.0.0.0-255.255.255.255&spr=https&sv=2019-12-12&sr=b&sig=azIJrrai%2Fwk187T78RwskS54BkQJD4JtNra5GbwHVCo%3D')
    paymentLookup = list(dfPayment.set_index('payment_type').to_dict().values()).pop()

    for row in dfTrip.itertuples():
        try:
            cursor.execute('''insert into NYCTAXI.TRIP(VENDOR_ID, PICKUP_DATETIME, DROPOFF_DATETIME, PASSENGER_COUNT, TRIP_DISTANCE, PICKUP_LONGITUDE, PICKUP_LATITUDE, RATE_CODE, STORE_AND_FWD_FLAG, DROPOFF_LONGITUDE, DROPOFF_LATITUDE, PAYMENT_TYPE, FARE_AMOUNT, SURCHARGE, TIP_AMOUNT, TOLLS_AMOUNT, TOTAL_AMOUNT) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                    row.vendor_id, row.pickup_datetime.split('T')[0] + ' ' + row.pickup_datetime.split('T')[1].split('+')[0].split('.')[0], row.dropoff_datetime.split('T')[0] + ' ' + row.dropoff_datetime.split('T')[1].split('+')[0].split('.')[0], row.passenger_count, row.trip_distance, row.pickup_longitude, row.pickup_latitude, row.rate_code, row.store_and_fwd_flag, row.dropoff_longitude, row.dropoff_latitude, paymentLookup[row.payment_type], row.fare_amount, row.surcharge, row.tip_amount, row.tolls_amount, row.total_amount)
        except: 
            print(row)

    # Commit the inserts on VENDOR table
    cursor.commit()


def main():
    etl()


if __name__ == '__main__':
    main()