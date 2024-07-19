# Ebben a listában tárolhatunk stringeket, amiket "" jellel fog
# eltárolni, valamint int számértékeket, amit nem "" jellel, csak simán tárol.
# A range-nél az első számjegy, ami alapértelmezettként 0, az benne van a range-ben,
# mig az utolsó szám, már nincs benne, igy ez 1-től 19-ig terjed. [x, y[
szamsor = []
for i in range(1, 20, 1):
    szamsor.append(i)
    if i > 9:
        break
# print(szamsor)

szam = int(input(f"Hányadik számra vagy kiváncsi? "
                 f"Ebben a listában {len(szamsor)} elem található. "))
print(f"Ebben a listában a {szam}. szám az a {szamsor[szam - 1]} ")