import smtplib, ssl

alicilar = []
context = ssl.create_default_context()

mail_adresi = str(input("---\nMail Adresinizi giriniz: "))
mail_sifresi = str(input("---\nMail şifrenizi giriniz: "))

mail_basligi = str(input("\nMail başlığı giriniz: "))

while True:
    alici_istek = str(input("---\nGeçmek için 'X' yazınız.\nMail Alıcılarını Yazınız: ")) 
    if alici_istek.lower() == "x":
        break
    if not alici_istek in alicilar:
        alicilar.append(alici_istek)

for gonderilecek_kisi in alicilar:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(mail_adresi, mail_sifresi)
        server.sendmail(mail_adresi, gonderilecek_kisi, "Python ile Gonderildi.\lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.")
        print(f"Mail, başarı ile '{gonderilecek_kisi}' adresine iletildi.")
