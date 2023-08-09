import re;

i = 1;

print("Loop While");
while i<10:
    print(i);
    i += 1;

print("Loop For");
x = 9;
for i in range (x):
    print("angka ke : ", i);
    i += 1;

print("Nested loop");
for baris in range (5):
    for kolom in range (7):
        print('o', end =" ");
    else:
        print(" ");


print("merubah huruf");
listkota = {'solo','Bandung','Bekasi','Jakarta'};

listhurufvocal = {'a','i','u','e','o'};

for kota in listkota:
    print('['+ kota +']');
    for vocal in listhurufvocal:
        print('--->' + re.sub('[aiueo]',vocal,kota));