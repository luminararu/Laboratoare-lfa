import parser
parsat=parser.load_file('inputfile')


states=[]
sf=[]
for stari in parsat['States']:
    if 'S' in stari :
        stari = stari.split(', ')
        states.append(stari[0])
        start=stari[0]
    if 'F' in stari:
        stari = stari.split(', ')
        states.append(stari[0])
        sf.append(stari[0])
    else:
        states.append(stari[0])

states = set(states)
s=set(parsat['Sigma'])


d={}
for tranz in parsat['Transitions']:
    elem = tranz.strip().split(', ')
    print(elem)
    if elem[0] not in d:
        d[elem[0]]={}
    d[elem[0]][elem[1]]=elem[2]



str=input()
current=start
for i in range(0, len(str)):
    if str[i] in s:
        current=d[current][str[i]]

if current in sf:
    print("acceptat")
else:
    print("nu e acceptat")



