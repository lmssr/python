def composition(brin):
    # Donne la composition du brin d'ADN

    compo={}
    for z in brin :
        compo[z] = compo.get(z, 0) + 1
    return compo

def pourcentGC(brin):
    # Donne le pourcentage de bases G et de bases C dans le brin

    result = composition(brin)
    pourcentGC = ( ( (float(result["g"]) + float(result["c"])) / float(len(brin) ) ) * 100.0)
    
    return pourcentGC

def tempFusionHowley(brin):
    # Donne temperature de fusion des sequences de plus de 10 nucleotides

    if len(brin) < 10:
        print("Erreur : la taille du brin doit etre superieur a 10 nucleotides")
        return

    Tm = 67.5 + ( 0.34 * pourcentGC(brin) ) - (395.0 / len(brin))
    
    return Tm

def estComplementaire(x, y):
    # Verifie si deux brins d'ADN (donnes dans la meme direction 5' -> 3' ou 3' -> 5') sont complementaires

    inversex = x[::-1]
    compx = ""

    nmax = len(x)

    for n in xrange(0, nmax):
        if inversex[n] == "a":
            compx += "t"
        if inversex[n] == "t":
            compx += "a"
        if inversex[n] == "c":
            compx += "g"
        if inversex[n] == "g":
            compx += "c"

    return compx == y

def ADN2ARN(seq):
    # Trancrit une chaine d'ADN en chaine d'ARN

    arn = ""
    nmax = len(seq)

    for n in xrange(0, nmax):
        if seq[n] == "a":
            arn += "u"
        if seq[n] == "t":
            arn += "a"
        if seq[n] == "c":
            arn += "g"
        if seq[n] == "g":
            arn += "c"

    return arn

def traduction(seq, x):
    # Traduit un brin d'ARN en acide amine, avec x le cadre de lecture

    if x <= 0 or x >= 2:
        print("Erreur : le cadre de lecture doit etre compris entre 0 et 2")
        return

    cg = {'uuu': 'F', 'ucu': 'S', 'uau': 'Y', 'ugu': 'C', 'uuc': 'F', 'ucc': 'S', 'uac': 'Y', 'ugc': 'C', 'uua': 'L', 'uca': 'S', 'uaa': '*', 'uga': '*', 'uug': 'L', 'ucg': 'S', 'uag': '*', 'ugg': 'W', 'cuu': 'L', 'ccu': 'P', 'cau': 'H', 'cgu': 'R', 'cuc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R', 'cua': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R', 'cug': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R', 'auu': 'I', 'acu': 'T', 'aau': 'N', 'agu': 'S', 'auc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S', 'aua': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R', 'aug': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R', 'guu': 'V', 'gcu': 'A', 'gau': 'D', 'ggu': 'G', 'guc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G', 'gua': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G', 'gug': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G', }
    aa = ""
    nmax = len(seq) - 2

    for n in xrange(x, nmax, 3):
        aa += cg[seq[n : n + 3]]

    return aa

def localiserMotifSimple(seq, motif, p = 0):
    # Recherche un motif simple dans une sequence d'ADN et retourne l'index de debut

    place = []
    
    n = p
    while n < len(seq):
        if p != seq.find(motif, n):
            p = seq.find(motif, n)
            if p != -1:
                place.append(p)
        p += 1

    return place

def signature(m):
    # Denombre tout les motifs pour une sequence de taille m

    if m <= 1 or m >= 10:
        print("Erreur : la taille de la sequence doit etre comprise entre 1 et 10")
        return

    return 4**m


