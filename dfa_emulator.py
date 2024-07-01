import parser
parsat=parser.load_file('inputfile')


states=[]
sf=[]

# separam starile si le introducem in vectorul states. De asemenea, extragem starea de inceput(in start) si cea de final in sf
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

# folosim un dictionar pentru a retine tranzitiile ( functia delta )
for tranz in parsat['Transitions']:
    elem = tranz.strip().split(', ')
    print(elem)
    if elem[0] not in d:
        d[elem[0]]={}
    d[elem[0]][elem[1]]=elem[2]



str=input()
current=start
# citim string ul si retinem starea curenta in current iar pentru ficare litera aplicam functia delta
for i in range(0, len(str)):
    if str[i] in s:
        current=d[current][str[i]]

# verificam daca ultima stare se afla in sf( final states)
if current in sf:
    print("acceptat")
else:
    print("nu e acceptat")



