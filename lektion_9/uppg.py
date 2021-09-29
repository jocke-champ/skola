import csv
import matplotlib.pyplot as plt
from uppg_6 import smooth_a, smooth_b


def load_csv(filename):
    filename = 'lektion_9/' + filename
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        dict = {row[1].lower(): list(map(float, row[3:])) for row in reader}
    return dict


def intersection(lista_1, lista_2):
    return list(set(lista_1).intersection(lista_2))


if __name__ == "__main__":
    data = load_csv('CO2Emissions_filtered.csv')
    landkod = ['dnk', 'fin', 'isl', 'nor', 'swe']
    colours = ['b', 'y', 'r', 'c', 'm']
    time = list(range(1960, 2015))
    data_landkod = {key: data[key] for key in data.keys() & landkod}

    fig, ax = plt.subplots()
    ax.set(
        xlabel='Year', ylabel='CO2 emissions (kt)',
        title='Yearly Emissions of CO2 in the Nordic Countries'
        )
    for country, c in zip(data_landkod.keys(), colours):
        ax.plot(
            time, data_landkod[country],
            color=str(c), linestyle='dotted'
            )
        ax.plot(
            time, smooth_a(data_landkod[country], 5),
            label=str(country), color=str(c), linestyle='solid'
            )
        ax.plot(
            time, smooth_b(data_landkod[country], 5),
            color=str(c), linestyle='dashed'
            )

    ax.legend()
    ax.grid()
    fig.savefig("test.png")
    plt.show()
