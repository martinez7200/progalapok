from cmath import pi


def kerulet(r):
    pi = 3.14
    return(2*r*pi)
def terulet(r):
    pi = 3.14
    return(r**2)*pi
sugar = float(input("A kör sugara: "))
K = kerulet(sugar)
T = terulet(sugar)
print("A kör kerülete: {0} egység.".format(K))
print("A kör területe: {0} négyzetegység.".format(T))