
import math


def muunna_xy_koordinaateiksi(kulma,vektori):
 #asteet = int(kulma*180/math.pi)
 x0 = round(vektori*math.cos(kulma), 0)
 y0 = round(vektori*math.sin(kulma), 0)
 x = int(x0)
 y = int(y0)
 return x, y