print("Idén is lesz programozás? ")
kerdes = input("Örülsz-e ennek? ")  # input-tal bekérünk a felhasználótól.
if kerdes == "i":
    print("De jó! ", end="\t")
elif kerdes == "n":
    print("Nemár! ", end="\t")  # \t a tabulátor, \n az enter.
else:
    print("Ezt nem tudom értelmezni! ", end="\t")
print("Hello ")
