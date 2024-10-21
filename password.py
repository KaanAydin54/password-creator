import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifreniz kaç karakterden oluşmalı ?"))
sifre = ""
for i in range (sayi):
    sifre += random.choice(karakterler)
    
print("Şifreniz:",sifre)
