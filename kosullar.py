meyve = input("Hangi meyveyi istiyorsun?")

if meyve ==("muz"):
     kilo = int(input("Kaç kilo muz istiyorsun?"))
     print(kilo*5,"tl ücret ödeyeceksiniz.")
#hello world
elif meyve ==("elma"):
     renk = input("Hangi renk elma istiyorsun?")
     if renk == ("kırmızı"):
         kilo = int(input("Kaç kilo kırmızı elma istiyorsun?"))
     elif renk ==("sarı"):
         kilo = int(input("Kaç kilo sarı elma istiyorsun?"))
     elif renk ==("yeşil"):
         kilo = int(input("Kaç kilo yeşil elma istiyorsun?"))
     else:
         print("Sadece sarı, kırmızı ya da yeşil renk elma var.")

     print(kilo*2,"tl ücret ödeyeceksiniz.")

elif meyve == ("üzüm"):
     renk = input("Hangi renk üzüm istiyorsun?")
     if renk == ("mor"):
        kilo = int(input("Kaç kilo mor üzüm istiyorsun?"))
        print(kilo*3,"tl ücret ödeyeceksiniz.")
     elif renk ==("yeşil"):
        kilo = int(input("Kaç kilo yeşil üzüm istiyorsun?"))
        print(kilo*3.5,"tl ücret ödeyeceksiniz.")
     else:
       print("Sadece mor ya da yeşil renk üzüm var.")
        
else:
     print("Manavda sadece muz, elma ve üzüm var.")
