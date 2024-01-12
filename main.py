meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
while True: 
    secim = input("eklemek için e sormak için s giriniz çıkmak için q giriniz")
    if secim == "q":
        print("çıkılıyor...")
        break
    elif secim == "e":
        key = input("kelimeyi büyük harf ile girinz = ")
        value = input("kelima nalmamını giriniz = ")
        meme_dict[key] = value
        if key not in meme_dict.keys():
            meme_dict[key] = value
            
    elif secim =="s":
            
        
        word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")
        
        if word in meme_dict.keys():
            # Kelime eşleşiyorsa ne yapmalıyız?
            print(meme_dict[word])
        else:
            
            print("sözlükte bu kelime bulunmamaktadır")
        
        
        
    else:
        print("hatalı giriş yaptınız")
