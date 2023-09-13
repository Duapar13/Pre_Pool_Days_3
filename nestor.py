NestorLeNFT="Bonjour1a1tous21je1suis1Albert1Nestor21le1castor31En1janvier1de1l4année1dernière21plus1de1dix5mille1personnes1m4ont1voués1un1culte31C4était1marrant21mais1un1peu1bizarre31En1tout1cas1plus1que1de1s4appeler1Albert1Nestor1en1étant1un1castor."
print(NestorLeNFT.replace("1" , " ")
      .replace("2" , ",")
      .replace("3" , ";")
      .replace("4" , "'")
      .replace("5" , "-")
      .replace("castor", "Castor", 1))
NestorCompte = str(NestorLeNFT.count("castor"))
print(" il y a " + NestorCompte + " Castor")
