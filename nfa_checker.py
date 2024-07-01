import parser
parsat=parser.load_file('inputfile')


states=[]
# se verifica parser s-a efectuat cu succes si se verifica daca exista o singura stare de start( variabila cnt retine aparitiile) si cel putin una de final
if parsat=={}:
    print("nu contine nimic")
else:
    s=set(parsat['Sigma'])
    cnt=0
    ok=False
    for stare in parsat['States']:
        stare=stare.strip()
        if 'S' in stare and 'F' in stare:
            cnt=cnt+1
            stare=stare.split(', ')
            states.append(stare)
            ok=True
            continue
        else:
            if 'S' in stare:
                cnt+=1
                stare=stare.split(', ')
                states.append(stare[0])
                continue
            if 'F' in stare:
                stare=stare.split(', ')
                ok=True
                states.append(stare[0])
                continue
            else:
                states.append(stare)

    if cnt!=1:
        ok=False
    if ok==False:
        print("nu contine nimic")
    print(states)
    print(s)
    # se verifica daca tranzitiile contin stari din state si litere aferenta alfabetului
    for tranz in parsat['Transitions']:
        elem=tranz.split(', ')
        print(elem)
        if elem[1] not in s and elem[1]!='epsilon':
            ok=False
            print("nu e bine")
        if elem[0] not in states:
            print("nu e bine")
            ok=False

    if ok == False:
        print("nu e bine")
    else:
        print("e ok")
