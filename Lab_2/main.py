import pandas as pd
import io
import requests
import plotter
import matplotlib.pyplot as plt


url_actual = "https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_settlement_actual.csv"
url_dynamics = "https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_settlement_dynamics.csv"
actual = requests.get(url_actual).content
dynamics = requests.get(url_dynamics).content

df_actual = pd.read_csv(io.StringIO(actual.decode('utf-8')))
df_dynamics = pd.read_csv(io.StringIO(dynamics.decode('utf-8')))

df_dynamics = df_dynamics.set_index("zvit_date")

region = "Закарпатська"

df_dynamics = df_dynamics[df_dynamics.registration_area == region]
df_dynamics = df_dynamics.groupby(df_dynamics.index).sum()


cols = [['new_susp'], ['new_confirm'], ['active_confirm'], ['new_death'], ['new_recover']]
plotter.plot(df_dynamics, cols)


df_grouped = df_actual.groupby(df_actual['registration_area'])[['total_susp', 'total_confirm', 'total_death', 'total_recover']].sum()
plt.bar(df_grouped.index, df_grouped["total_confirm"])
plt.xticks(rotation=40)
plt.show()


map = plt.imread('super.jpg')
fig, ax = plt.subplots()
ax.scatter(df_actual.registration_settlement_lng, df_actual.registration_settlement_lat,
           s=df_actual.total_confirm//40, color="red")
ax.imshow(map, extent=[21.8, 40.4, 44.2, 52.8])
ax.set_xlim(20, 42)
ax.set_ylim(43, 55)
plt.show()


df_grouped.to_excel('covid_by_region.xlsx')
df_dynamics.to_excel('covid_transcarpatian.xlsx')