liste = ["Cat","Garden","Mice"]
chaine = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()

for i in chaine:
    nb1 = chaine.count(liste[0].lower()) + chaine.count(liste[1].lower()) + chaine.count(liste[2].lower())
for i in chaine:
    nb2 = chaine[::-1].count(liste[0].lower()) + chaine[::-1].count(liste[1].lower()) + chaine[::-1].count(liste[2].lower())

print(nb1+nb2)