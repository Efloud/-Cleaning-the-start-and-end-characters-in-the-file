import time
print(
 """                                                                                           
▓█████   █████▒▄████▄   ██▓    ▓█████ ▄▄▄       ██▀███  
▓█   ▀ ▓██   ▒▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ▓██ ▒ ██▒
▒███   ▒████ ░▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒
▒▓█  ▄ ░▓█▒  ░▒▓▓▄ ▄██▒▒██░    ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  
░▒████▒░▒█░   ▒ ▓███▀ ░░██████▒░▒████▒▓█   ▓██▒░██▓ ▒██▒
░░ ▒░ ░ ▒ ░   ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░
 ░ ░  ░ ░       ░  ▒   ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░
   ░    ░ ░   ░          ░ ░      ░    ░   ▒     ░░   ░ 
   ░  ░       ░ ░          ░  ░   ░  ░     ░  ░   ░     
              ░                                         
""", '\n')

time.sleep(1.0)
location = input("[x] Temizlemek istediğiniz Dosya konumunu Girin => ")

if not location.endswith("txt"):
    print("lütfen uzantıyı txt olarak verin.")

for i in location:
    rep = i.replace("/", "\\")

try:

    with open(location, "r") as file:
        read = file.read()
        print("\n")
        time.sleep(1.0)
        clear = input("[+] Temizlemek İstediğiniz Karakterler ? => ")
        print("\n")
        time.sleep(1.0)
        save = input("[+] Dosyanın Kaydedileceği Konumu Girin : ")
        output = open(save, 'w', encoding='utf-8')

    for i in read.split():
        print(i.strip(clear), end="\n", file=output)

    print("\n", f"[+] Dosya : {save} konumuna kaydedildi.", sep="")

except FileNotFoundError:
    print("Belirtmiş olduğunuz Dosya Konumu Bulunamadı !")
