meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir",
            "GOTİK":"Kişi için kullanılırsa garip ,tuhaf anlamlarına gelir ,türkçedeki MAL argo kelimesine oldukça benzemektedir",
            "Solitary": "Kendi tercihiyle veya yapısı gereği tek başına olan",
            "Lose one's mind": "Kafayı sıyırmak, delirmek"
            }

kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print(meme_sozlugu[kelime])
else:
    print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
