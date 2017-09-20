import random

nome = 'jubilu'
l = list(nome)
while l[1] != 'i':
    random.shuffle(l)
    print(l)

for i in range(1,11):
    j = i*i
    k = j + j
    print(i, j, k)
print('\n')
print('FIM')

print('\n')

estados = {'Santa Catarina': 'SC', 'Paraná': 'PR', 'São Paulo': 'SP'}

print(estados)
for estado in estados:
    print(estado)
print('\n')

# i = 0
# j = 1024
# k = 0
# while i >= 0:
#     k = j + 1024
#     print(j**k)
#

m = 'Euro'
t = 2.7383

f = 'O %s está cotado a R$ %0.2f.' %(m,t)
print(f)


s = "parabens!"
l = list(s)
l2 = [ord(x) for x in l]
l3 = [chr(x) for x in l2]
s2 = "".join(l3)
print(s)
print(l)
print(l2)
print(l3)
print(s2)