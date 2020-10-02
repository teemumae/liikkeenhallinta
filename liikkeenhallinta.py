
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
    x0 = hahmo["x"]
    y0 = hahmo["y"]
    print("Hahmo on sijainnissa ({}, {})", x, y)
    suunta = float(input("Anna liikkumissuunta asteina: "))
    nopeus = float(input("Anna liikenopeus: "))
    hahmo["suunta"] = suunta
    hahmo["nopeus"] = nopeus


def paivita_sijainti(hahmo):
    nopeus = hahmo["nopeus"]
    suunta = hahmo["suunta"]