#Python: Bir Yazı İçerisinde Bulunan Kelimeleri Veya Karekterleri Ayırarak Bir Diziye Atamak
#Online eğitimler için: https://www.excelsizeyeter.com/excelsizeyeter.com/udemy_giris.php adresine tıklayınız.
yazı="Selam herkese, burada bazı sayılar var. Bunlar: 1, 2, 3, 4, 5"
dizi1=yazı.split()#Eğer parantez içerisine herhangi bir şey yazılmazsa bu durumda boşluğu baz alır.
dizi2=yazı.split(",")#Parantez içerisine herhangi bir şey yazıldığında o karakteri ayraç olarak görür ve dizi oluşturur.
print(dizi1)
print(dizi2)
