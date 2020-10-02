
import math
hahmo_1 = {
    "x": 0,
    "y": 0,
    "suunta": 0,
    "nopeus": 0
}

hahmo_2 = {
    "x": 50,
    "y": 50,
    "suunta": 0,
    "nopeus": 0
}

def muunna_xy_koordinaateiksi(kulma,vektori):
 kulma_radiaanit = math.radians(kulma)
 x0 = round(vektori*math.cos(kulma_radiaanit), 0)
 y0 = round(vektori*math.sin(kulma_radiaanit), 0)
 x = int(x0)
 y = int(y0)
 return x, y

def kysy_liike(hahmo):
    x = hahmo["x"]
    y = hahmo["y"]
    print("Hahmo on sijainnissa ({},  {})".format(x, y))
    suunta = float(input("Anna liikkumissuunta asteina: "))
    nopeus = float(input("Anna liikenopeus: "))
    hahmo["suunta"] = suunta
    hahmo["nopeus"] = nopeus


def paivita_sijainti(hahmo):
    nopeus = hahmo["nopeus"]
    suunta = hahmo["suunta"]
    x0 = hahmo["x"]
    y0 = hahmo["y"]
    x, y = muunna_xy_koordinaateiksi(suunta, nopeus)
    x2 = x0 + x
    y2 = y0 + y
    hahmo["x"] = x2
    hahmo["y"] = y2

print("Pelaajan 1 vuoro")
kysy_liike(hahmo_1)
paivita_sijainti(hahmo_1)
x1 = hahmo_1["x"]
y1 = hahmo_1["y"]
print("Uusi sijainti:({}, {})".format(x1,y1))
print("Pelaajan 2 vuoro")
kysy_liike(hahmo_2)
paivita_sijainti(hahmo_2)
x2 = hahmo_2["x"]
y2 = hahmo_2["y"]
print("Uusi sijainti:({}, {})".format(x2,y2))
