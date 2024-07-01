
# parser ul imparte sectiunile din input file si returneaza un dictionar cu toate
def load_file(filename):
    d={}
    f = open(filename, 'r')
    curent_state=None
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        if line[0]=='#':
            continue
        if ':' in line:
            curent_state=line.replace(':', '')
            curent_state=curent_state.strip()
            d[curent_state]=[]
        elif curent_state is not None and line!='End':
                d[curent_state].append(line)
        if line=='End':
            curent_state=None
    return d
