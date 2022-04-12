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

location = input("[x] Temizlemek istediğiniz Dosya konumunu Girin => ")

if not location.endswith("txt"):
    print("txt girin !")
    quit()
   
for i in location:
    rep = i.replace("/", "\\")

try:

    with open(location, "r") as file:
        read = file.read()
        print("\n")
        time.sleep(0.5)
        clear = input("[+] Temizlemek İstediğiniz Karakterler ? => ")
        print("\n")
        time.sleep(0.5)
        save = input("[+] Dosyanın Kaydedileceği Konumu Girin : ")

        if not save.endswith("txt"):
            print("txt girin !")
            quit()
           
        output = open(save, 'w', encoding='utf-8')


    for i in read.split():
        print(i.strip(clear), end="\n", file=output)

    time.sleep(0.5)
    print("\n", f"[+] Dosya : {save} konumuna kaydedildi.", sep="")

except FileNotFoundError:
    print("Dosya Konumu Bulunamadı !")

 
