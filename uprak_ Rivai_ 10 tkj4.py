# Rumus Volume Balok
print ("\n1.Volume Balok")
panjang = int(input(" 5 :"))
lebar= int(input("10: "))
tinggi= int(input("15: "))
volume_balok = panjang * lebar * tinggi

print ("Volume Balok Adalah",volume_balok)

# Rumus Volume Kubus
print ("\n2.Volume Kubus")
sisi = int(input("5: "))
volume_kubus = sisi * sisi * sisi

print ("Volume kubus adalah", volume_kubus)

# Rumus Volume Limas
print ("\n3.Volume Limas")
sisi_l = int(input("5: "))
tinggi_l = int(input("6: "))
luas_l = sisi_l * sisi_l
volume_limas = luas_l * tinggi_l

print ("volume limas adalah",volume_limas)

# Rumus volume tabung
print ("\n4. Volume Tabung")
r = int(input("7: "))
tinggi_t = int(input("10: "))
volume_tabung = 22/7 * r * r * tinggi_t

print ("volume tabung adalah",volume_tabung)

# Celcius Ke Reamur
print ("\n5.Celcius ke Reamur")
C = int(input("40: "))
Reamur = 4/5 * C

print ("Celcius ke Reamur adalah",Reamur)
