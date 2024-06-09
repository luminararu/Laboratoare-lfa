import parser
parsat=parser.load_file('inputfile')

if parsat=={}:
    print("nu contine nimic")
else:
    s=set(parsat['Sigma'])
    print(s)
    cnt=0
    ok=False
    for stari in parsat['States']:
        if 'S' in stari:
            cnt+=1
        if 'F' in stari:
            ok=True
    if cnt!=1:
        ok=False

    states=[]
    if ok==False:
        print("nu e bine")
    for stari in parsat['States']:
        if 'S' in stari or 'F' in stari:
            stari=stari.split(', ')
            states.append(stari[0])
        else:
            states.append(stari)


    states=set(states)
    for tranz in parsat['Transitions']:
        elem=tranz.strip().split(', ')
        if elem[1] not in s or elem[0] not in states:
            ok=False
    if len(states)*len(s)==len(parsat['Transitions']):
        ok=True
    else:
        ok=False
    if ok==False:
        print("nu e bine")
    else:
        print("e ok")
