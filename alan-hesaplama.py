# -*- coding: utf-8 -*-
 
metin=input("Metni Giriniz: ")
count=0
while count < len(metin):
  print(metin[count])
  count += 1
 
 
#not1 = int(input("1.Notu Girin : "))
yazili1 = int(input('1. Yazılı : '))
yazili2 = int(input('2. Yazılı : '))
yazili3 = int(input('3. Yazılı : '))
ortalama=(yazili1+yazili2+yazili3)/3
print("Yazılı Ortalaması :{0} ".format(ortalama))
