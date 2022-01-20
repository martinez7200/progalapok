egyik = input("Adj meg egy szót! ")
masik = input("Adj meg egy másik szót! ")
if len(egyik) > len(masik):
    print("Az első szó a hosszabb! ")
elif len(egyik) < len(masik) :
    print("A másik szó a hosszabb!" )
else:
    print("Egyenlő hosszú a két szó! ")