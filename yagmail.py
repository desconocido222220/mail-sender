import yagmail

alicilar = []

mail_adresi = str(input("---\nMail Adresinizi giriniz: "))
mail_sifresi = str(input("---\nMail şifrenizi giriniz: "))
mail_basligi = str(input("---\nMail başlığı giriniz: "))
mail_icerigi = str(input("---\nMail içeriğinin bulunduğu txt dosyasını giriniz: "))

with open(f"{mail_icerigi}.txt", "r", encoding="utf-8") as dosya:
    mail_icerigi = dosya.read()

while True:
    alici_istek = str(input("---\nGeçmek için 'X' yazınız.\nMail Alıcılarını Yazınız: ")) 
    if alici_istek.lower() == "x":
        break
    if not alici_istek in alicilar:
        alicilar.append(alici_istek)
        
for alici in alicilar:
    yag = yagmail.SMTP(mail_adresi, mail_sifresi)
    yag.send(
        to = alici,
        subject = mail_basligi,
        contents = mail_icerigi, 
    )
    print(f"Başarıyla '{alici}' mailine yollandı.")
