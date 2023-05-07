ürün = {
    "ad":"",
    "fiyat":"",
    "ürün sayısı":"",
}

s = 0

while s < 6:
    if s == 0:
        ad = str(input("ürünün adı nedir:"))
        ürün["ad"]=ad
        s+=1
    if s == 1:
        fiyat = str(input("ürünün fiyatını giriniz:"))
        ürün["fiyat"]=fiyat
        s+=1
    if s == 2:
        sayı = str(input("ürün sayısını giriniz:"))
        ürün["ürün sayısı"]=sayı
        s+=1
    if s == 3:
        değiş = int(input("değiştirmek istediğiniz yapı varmı varsa 1 basınız yoksa 2 ye:"))    
        if değiş == 1:
            hangi = int(input("hangi ürünü değiştirceksiniz (adı değiştircekseniz 1 e) (fiyat değiştircekseniz 2 e) (ürün sayısını değiştircekseniz 3 e basınız):"))
            if hangi == 1:
                print(ürün["ad"])
                ad1 = str(input("neyle deiştreceksiniz:"))
                ürün["ad"]=ad1
            if hangi == 2:
                print(ürün["fiyat"])
                fiyat1 = str(input("neyle deiştreceksiniz:"))
                ürün["fiyat"]=fiyat1
            if hangi == 3:
                print(ürün["ürün sayısı"])
                sayı1 = str(input("neyle deiştreceksiniz:"))
                ürün["ürün sayısı"]=sayı1
    if değiş == 2:
        s+=1      
    if  s == 4:
        ekle = int(input("katagori eklemek isterseniz 1 istemezseniz 2 ye basınız:"))
        if ekle == 1:
            katagori = str(input("ekleme yapmak istediğiniz katagorinin adı:"))
            katagori1 = str(input("katagoriye eklemek istediğiniz şey:"))
            ürün[katagori]=katagori1
    if ekle == 2:
        s+=1
        break
    
           
        
    
    
s+=1
print(ürün)