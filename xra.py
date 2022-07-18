defuser = "Xra"
defkey = "şifre"

while (True):
    user = input("E-posta: ")
    key = input("Discord Şifreniz:")

    if (defuser == user) and (key == defkey):
        print("Girişiniz başarıyla sağlandı")
        break
    elif (defuser != user) and (key == defkey):
        print("Kullanıcı isminiz uyuşmiyor.")
    elif (defuser == user) and (key != defkey):
        print("Şifreniz uyuşmiyor.")

        sifremiunuttum = input( )
        if (sifremiunuttum == "şifremi unuttum"):
            yenikey = input("Yeni şifre giriniz 😊")
            print("Lütfen bekleyin...")
            defkey = yenikey
            print("Şifre başarıyla değiştirildi")
            print(" ")

    else:
        print("Tekrar deneyin.")