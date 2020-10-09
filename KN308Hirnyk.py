import pandas as pd
from datetime import datetime
import KN308Hirnyk1 as plotter


columns = ['Temperature', 'Dew Point', 'Humidity', 'Wind', 'Wind Speed', 'Wind Gust', 'Pressure',
           'Precip.', 'Precip Accum', 'Condition']


def convert(db):
    db['Humidity'] = db['Humidity'].apply(lambda x: x.replace('%', '')).astype('int64')
    db['Wind Speed'] = db['Wind Speed'].apply(lambda x: x.replace(' mph', '')).astype('int64')
    db['Wind Gust'] = db['Wind Gust'].apply(lambda x: x.replace(' mph', '')).astype('int64')
    db['Wind'] = db['Wind'].astype('category')
    db['Condition'] = db['Condition'].astype('category')
    db['day/month'] = db['day/month'].apply(lambda x: x.replace('.', '') + "2020")
    db['day/month'] = pd.to_datetime(db['day/month'])
    db['day/month'] = db['day/month'].apply(lambda x: x.strftime("%m/%d/%Y"))
    db['Time'] = db['Time'].apply(lambda x: datetime.strptime(x, "%I:%M %p").strftime('%H:%M'))


db = pd.read_csv('D:\Labs_PP\IAD_Lab1\DATABASE.csv', sep=';')
convert(db)
db = db.set_index('day/month')

print('Hello')

while True:
    print('To draw graph with one parament(y) write 1, for two paramatres write 2, to show graphs - 3')
    command = int(input())
    if command == 1:
        print('Enter columns[' + ', '.join(columns) + ']')
        columns = input().split(',')
        print('Enter type of graphic [' + ', '.join(plotter.graph_types_for_one) + ']')
        kind = input()
        for column in columns:
            plotter.plot(db, kind, column)
    elif command == 2:
        print('Enter two columns[' + ', '.join(columns) + ']')
        columns = input().split(',')
        print('Enter type of graphic [' + ', '.join(plotter.graph_types_for_two) + ']')
        kind = input()
        plotter.plot(db, kind, columns)
    elif command == 3:
        plotter.show()
