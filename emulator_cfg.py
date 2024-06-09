import parser
parsat = parser.load_file('inputcfg')

s = set(parsat["Sigma"])

#funcția pentru numararea literelor dintr-un sir
def nr_litere(stri):
    cnt = 0
    for i in range(len(stri)):
        if stri[i] in s:
            cnt += 1
    return cnt

d = {}

# Prelucrarea starilor si identificarea simbolului de start
new_states = []
start = None
for elem in parsat["States"]:
    if 'S' in elem:
        elem = elem.split()[0]
        start = elem
    new_states.append(elem)
parsat["States"] = new_states
states = set(parsat["States"])

# Verificare simbol de start
if not start:
    print("Eroare: Nu există un simbol de start definit.")
    exit(1)

# Prelucrarea regulilor
for rule in parsat["Rules"]:
    lhs, rhs = rule.split(' ', 1)  # Split on first space only
    if lhs not in d:
        d[lhs] = []
    d[lhs].append(rhs)

# Lista pentru parcurgerea curenta si cea nouă
parc_curent = [start]

# Sirul de verificat
st = input("Introduceți șirul de verificat: ")

# Variabila ok pentru controlul buclei
ok = True

# Parcurgerea regulilor pentru generarea șirurilor posibile
while ok:
    parc_new = []
    for rul in parc_curent:
        for i in range(len(rul)):
            if rul[i] in states:
                for elem in d[rul[i]]:
                    new_rul = rul[:i] + elem + rul[i+1:]
                    parc_new.append(new_rul)

    # Filtrarea șirurilor generate pentru a limita lungimea
    parc_new = [elem for elem in parc_new if nr_litere(elem) <= len(st)]

    # Dacă nu s-au generat noi șiruri, oprim bucla
    if not parc_new:
        break

    # Actualizarea listei de parcurgere curentă
    parc_curent = parc_new[:]

    # Verificarea dacă șirul de verificat a fost generat
    if st in parc_curent:
        ok = False
        break

# Verificarea finală dacă șirul de verificat este generat de gramatică
if st in parc_curent:
    print("Șirul este acceptat de gramatică.")
else:
    print("Șirul nu este acceptat de gramatică.")
