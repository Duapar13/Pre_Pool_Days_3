liste = ["Cat","Garden","Mice"]
chaine = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()

for i in chaine:
    nb1 = chaine.count(i.lower())
for i in chaine:
    nb2 = chaine[::-1].count(i.lower())

print(nb1+nb2)