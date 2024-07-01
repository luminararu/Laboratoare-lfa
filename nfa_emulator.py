import parser

parsat=parser.load_file('inputfile')

states=[]
sf=[]
# se extrag starile si se retine starea de inceput si starea de final analizandu-se  cazurle in care pe o linie avem S, F sau S si F( starea de inceput este si stare de final)
for stare in parsat['States']:
    if 'S' in stare and 'F' in stare:
        stare = stare.split(', ')
        states.append(stare[0])
        start=stare[0]
        sf.append(stare[0])
        continue
    else:
        if 'S' in stare:
            stare = stare.strip().split(', ')
            states.append(stare[0])
            start=stare[0]
            continue
        if 'F' in stare:
            stare = stare.strip().split(', ')
            states.append(stare[0])
            sf.append(stare[0])
            continue
        else:
            states.append(stare)

states = set(states)
s=set(parsat['Sigma'])

d={}

# se retin tranzitiile intr-un dicionar care va definii functia delta 
for tranz in parsat['Transitions']:
    elem = tranz.strip().split(', ')
    print(elem)
    if elem[0] not in d:
        d[elem[0]]={}
    if elem[1] not in d[elem[0]]:
        d[elem[0]][elem[1]]=[]

    d[elem[0]][elem[1]].append(elem[2])

st=input()
# parc_curent va retine elemente care sunt parcurse simulta la momentul citirii
parc_curent=[]
index=0
parc_curent.append(start)

# se parcurge string ul si se aplica funtia delta pentru fiecare stare din parcurgerea curenta creandu-se astfel un nou vector parc_new care va fi nou parc_curent
for i in range(0, len(st)):
    parc_new=[]
    for star in parc_curent:
        for starc in d[star][st[i]]:
            parc_new.append(starc)
    parc_curent=parc_new

if any(element in parc_curent for element in sf):
    print("accepta")
else:
    print("nu accepta")
