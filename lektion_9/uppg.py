import csv
import matplotlib.pyplot as plt


def load_csv(filename):
    with open('lektion_9/' + filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        dict = {row[1].lower(): list(map(float, row[3:])) for row in reader}
    return dict


# print(load_csv('CO2Emissions_filtered.csv'))
data = load_csv('CO2Emissions_filtered.csv')
landkod = ['dnk', 'fin', 'isl', 'nor', 'swe']
time = list(range(1960, 2015))
data_landkod = {key: data[key] for key in data.keys() & landkod}

fig, ax = plt.subplots()
ax.plot(time, data_landkod.values())

ax.set(
    xlabel='Year', ylabel='CO2 emissions (kt)', title='Yearly Emissions of CO2 in the Nordic Countries'
    )
ax.grid()

fig.savefig("test.png")
plt.show()
