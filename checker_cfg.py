import parser

parsat = parser.load_file('inputcfg')

states = []
# se verifica daca parsarea s-a efectuat cu succes si se extrag variabilele( aici au nume de states) verificandu-se existenta starii de inceput 

ok= False
if parsat == {}:
    print("nu contine nimic")
else:
    new_states=[]
    for elem in parsat["States"]:
        if 'S' in elem:
            elem=elem.split()
            elem=elem[0]
            ok=True
        new_states.append(elem)
    parsat["States"] = new_states
    states = set(parsat["States"])
    sigma = set(parsat["Sigma"])
    print(parsat)
    print("States:", states)
    print("Sigma:", sigma)

    # se verifica daca regulile sunt bine definte ( fiecare variabila se afla in variables si fiecare litera se afla in Sigma)
    for rul in parsat["Rules"]:
        rul = rul.strip().split()
        if len(rul) != 2:
            ok = False
            print(f"Regula incorectă: {rul}")
            continue
        lhs, rhs = rul

        if lhs not in states:
            ok = False
            print(f"Starea din partea stângă a regulii {lhs} nu este în stările definite.")

        for char in rhs:
            if char not in sigma and char not in states and char != '':
                ok = False
                print(f"Caracterul {char} din partea dreaptă a regulii nu este în Sigma sau States.")

if ok == False:
    print("nu e bine")
else:
    print("e bine")
