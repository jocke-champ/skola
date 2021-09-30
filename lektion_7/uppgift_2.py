import re

primitives = ['for', 'in', 'if', 'else', 'def']

filnamn = 'lektion_7/testprogram'
fil = open(filnamn + '.py', 'r')
text = fil.readlines()
fil.close()

for line in enumerate(text):
    text[line[0]] = re.sub(r'#.*$', '', line[1]).replace('\n', '').rstrip()

    if (re.search(r'(?<=#)(.*)', line[1])):
        kommentar = '#' + re.search(r'(?<=#)(.*)', line[1]).group(1)
    else:
        kommentar = ''
    ut = open(filnamn + '.ut.py', 'a')
    ut.write(
        str(line[0]+1) + ' ' + text[line[0]] + '\t\t\t' + kommentar + '\n')
    ut.close()

unika = []
for i in enumerate(text):
    for ord in re.findall(r'[^\d\W]+', text[i[0]]):
        if ord not in unika and ord not in primitives:
            unika.append(ord)
unika.sort()
ref_lista = ['' for i in range(len(unika))]

for i in enumerate(text):
    for ord in re.findall(r'[^\d\W]+', text[i[0]]):
        if ord not in primitives:
            if ref_lista[unika.index(ord)] == '':
                ref_lista[unika.index(ord)] += str(i[0]+1)
            else:
                ref_lista[unika.index(ord)] += ', ' + str(i[0]+1)

ut = open(filnamn + '.ut.py', 'a')
ut.write("\n\n\nReferenslista:")
for i in enumerate(unika):
    ut.write('\n\t\t' + unika[i[0]] + '\t\t\t' + '[' + ref_lista[i[0]] + ']')
ut.close()
