# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib.ticker import StrMethodFormatter
import connection as conn



def question1():
    cnxn = conn.sqlConnect()
    data = pd.read_sql('''select year(DROPOFF_DATETIME) YEAR, round(avg(TRIP_DISTANCE),3) AVERAGE from NYCTAXI.TRIP where PASSENGER_COUNT <= 2 group by year(DROPOFF_DATETIME)''', cnxn)
    style.use('seaborn-deep')
    data.plot(kind = 'bar', x = 'YEAR', y = 'AVERAGE', title ="Average distance traveled by trips with a maximum of 2 passengers per year", grid=False, xlabel = 'Year', ylabel = 'Average', legend=False, figsize=(9,6), color='#D8300C', zorder=2)
    plt.show()


def question2():
    cnxn = conn.sqlConnect()
    data = pd.read_sql('''select top(3) V.NAME, round(sum(T.TOTAL_AMOUNT),2) TOTAL_AMOUNT from NYCTAXI.TRIP T inner join NYCTAXI.VENDOR V on T.VENDOR_ID = V.VENDOR_ID group by V.NAME order by round(sum(T.TOTAL_AMOUNT),2) desc''', cnxn)
    style.use('seaborn-deep')
    plt.rcParams.update({'font.size': 8, 'figure.autolayout': True})
    data.plot(kind = 'bar', x = 'NAME', y = 'TOTAL_AMOUNT', title ="3 biggest vendors in total amount of money raised", xlabel = 'Vendor', ylabel = 'Total amount', legend=False, figsize=(8,8), color='#13A9A8', zorder=2, width = 0.7) 
    plt.show()


def question3():
    cnxn = conn.sqlConnect()
    data = pd.read_sql('''select DATEADD(month, DATEDIFF(month, 0, DROPOFF_DATETIME), 0) MONTH, count(1) QUANTITY from (select cast(DROPOFF_DATETIME as date) DROPOFF_DATETIME from NYCTAXI.TRIP where PAYMENT_TYPE = 'Cash') as AUX group by DATEADD(month, DATEDIFF(month, 0, DROPOFF_DATETIME), 0) order by DATEADD(month, DATEDIFF(month, 0, DROPOFF_DATETIME), 0)''', cnxn)
    data['MONTH_YEAR'] = data['MONTH'].dt.to_period('M')
    data.plot(kind = 'bar', x = 'MONTH_YEAR', y = 'QUANTITY', title ="Number of runs paid in cash monthly", grid=False, xlabel = 'Year/Month', ylabel = 'Quantity', legend=False, figsize=(12,8), color='#8C19B1', zorder=2, width=1.0)    
    plt.show()


def question4():
    cnxn = conn.sqlConnect()
    data = pd.read_sql('''select cast(DROPOFF_DATETIME as date) DAY, round(sum(TIP_AMOUNT),2) TIP_AMOUNT from NYCTAXI.TRIP where year(DROPOFF_DATETIME) = 2012 and month(DROPOFF_DATETIME) in (10, 11, 12) group by cast(DROPOFF_DATETIME as date) order by cast(DROPOFF_DATETIME as date)''', cnxn)
    data.plot(kind = 'line', x = 'DAY', y = 'TIP_AMOUNT', title ="Number of daily tips in the last 3 months of 2012", grid=False, xlabel = 'Day', ylabel = 'Tip amount', legend=False, figsize=(12,8), color='#86bf91', zorder=2)    
    plt.show()


def question5():
    cnxn = conn.sqlConnect()
    data = pd.read_sql('''select year(DROPOFF_DATETIME) YEAR, avg(datediff(minute, PICKUP_DATETIME, DROPOFF_DATETIME)) MINUTES from NYCTAXI.TRIP where datename(dw, DROPOFF_DATETIME) in ('Saturday', 'Sunday') group by year(DROPOFF_DATETIME) order by year(DROPOFF_DATETIME)''', cnxn)
    data.plot(kind = 'bar', x = 'YEAR', y = 'MINUTES', title ="Average race time on Saturday and Sunday per year", grid=False, xlabel = 'Year', ylabel = 'Minutes', legend=False, figsize=(8,6), color='#E3E61E', zorder=2)    
    plt.show()

