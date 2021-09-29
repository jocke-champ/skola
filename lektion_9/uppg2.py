import matplotlib.pyplot as plt
from uppg import load_csv, intersection


data_popu = load_csv('population.csv')
data_pollu = load_csv('CO2Emissions_filtered.csv')
countries = intersection(list(data_popu), list(data_pollu))

fig, ax = plt.subplots()
ax.set(
    xlabel='Population', ylabel='CO2 Emmissions in 2014 (kt)',
    title='CO2 Emmissions vs. population'
)

x = [data_popu[c][-5] for c in countries]
y = [data_pollu[c][-1] for c in countries]

ax.scatter(x, y)

for i, country in enumerate(countries):
    ax.annotate(country, (x[i], y[i]))
    
# landskod = ['bol', 'ven', 'chl', 'ecu', 'pry']
# time = range(1800, 2019)
# data_landkod = {key: data[key] for key in data.keys() & landskod}


# fig, ax = plt.subplots()
# ax.set(
#     xlabel='Year', ylabel='population count',
#     title='Population growth'
#     )
# for country in data_landkod.keys():
#     ax.plot(
#         time, data_landkod[country], label=str(country)
#         )


ax.legend()
ax.set_yscale('log')
ax.set_xscale('log')
# ax.grid()
fig.savefig("test.png")
plt.show()
