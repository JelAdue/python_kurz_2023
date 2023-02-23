#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# 1. Vytvoř seznam průměrných teplot pro každý den.
prumerene_teploty = [round(sum(mereni)/len(mereni),1) for mereni in teploty]

print(prumerene_teploty)

# 2. Vytvoř seznam ranních teplot.
ranni_teploty = [mereni[0] for mereni in teploty]

print(ranni_teploty)

# 3. Vytvoř seznam nočních teplot.
nocni_teploty = [mereni[-1] for mereni in teploty]

print(nocni_teploty)

# 4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_a_nocni_teploty = [[mereni[1], mereni[-1]] for mereni in teploty]

"""poledni_a_nocni_teploty = []
for mereni in teploty:
    poledni_a_nocni_teploty.append([mereni[1], mereni[-1]])"""

print(poledni_a_nocni_teploty)