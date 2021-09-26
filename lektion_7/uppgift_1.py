import re


def bara_ord(lista):
    lista = [re.findall(r'[a-zA-ZåäöÅÄÖ]+', e) for e in lista]
    return [i[0] for i in lista]


def las_in(filnamn):
    return open(filnamn).read().lower().split()


def main():
    m = int(input('m val: '))
    n = int(input('n val: '))
    filnamn = 'lektion_7/test.txt'
    fil = bara_ord(las_in(filnamn))

    unika = []
    for ord in fil:
        if ord not in unika:
            unika.append(ord)

    antal = []
    for unik in unika:
        ant = 0
        for ord in fil:
            if ord == unik:
                ant += 1
        antal.append((ant, unik))

    print('antal ord:', len(fil))
    print('antal unika ord:', len(unika))
    print(f'\nantalet {n} vanligaste:')

    antal.sort()
    for i in range(n):
        ant, ord = antal[i]
        print(ord, ant)
    print(f'\nantalet {m} ovanliga:')

    antal.reverse()
    for i in range(m):
        ant, ord = antal[i]
        print(ord, ant)


if __name__ == "__main__":
    main()
