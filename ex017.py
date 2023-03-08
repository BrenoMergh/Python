from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
#hip = math.sqrt(math.pow(ca,2)+math.pow(co,2))
hip = hypot(co,ca)
print(hip)