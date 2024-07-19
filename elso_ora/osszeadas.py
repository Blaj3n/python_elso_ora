print("összeadás gyakorlat ")
print(f"\n\tAdj meg két számot! ")  # \t -> tab, \n -> enter.
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek még egy számot: "))
osszeg = szam1 + szam2
tipp = int(input("Mennyi a két szám összege? "))
if tipp == osszeg:
    print("Helyes az eredmény! ")
elif tipp != osszeg:
    print("Sajnos nem helyes az eredmény! ")
    print(f"A helyes eredmény: {osszeg} ")