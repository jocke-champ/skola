import re


def rakna_ant(ord, mening):
    return mening.lower().split().count(ord)


def ord_mest_anvanda(m):


def ord_minst_anvanda(n):
    sd


unika_ord = []
unika_ord = 0
ord = {}
text = ''
filnamn = 'lektion_7/test.txt'
with open(filnamn, 'r') as f:
    unika_ord = list(set(f.readlines()))
    text = re.sub(r'#.*$', '', f.readlines()) 
    unika_ord = [ord_i.replace(".", "") for ord_i in unika_ord[0].split(' ')]
    ant_unika_ord = len(unika_ord)
    ord = dict.fromkeys(unika_ord, 0)
    for i in range(unika_ord):
        ord[i] = rakna_ant(unika_ord[i], text)


print('Antal ord:', ant_unika_ord)
print('Alla ord:', str(unika_ord))
print('Mest anvanda ordet:', max(ord, key=ord.get))
print('Minst anvanda ordet:', min(ord, key=ord.get))
