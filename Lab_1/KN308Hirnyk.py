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


db = pd.read_csv('D:\Labs_PP\IAD_Lab1\DATABASE.csv', sep=';', decimal=',')
convert(db)
db = db.set_index('day/month')


cols = [['Wind'], ['Condition'], ['Wind Speed'], ['Wind Gust', 'Temperature']]

plotter.plot(db, cols)


