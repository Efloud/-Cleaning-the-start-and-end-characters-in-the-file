#python3
print(
 """                                                                                           
@@@@@@@   @@@       @@@@@@@@  @@@@@@    @@@@@@@   
@@@@@@@@  @@@       @@@@@@@@  @@@@@@@@  @@@@@@@@  
!@@       @@!       @@!       @@!  @@@  @@!  @@@  
!@!       !@!       !@!       !@!  @!@  !@!  @!@  
!@!       @!!       @!!!:!    @!@!@!@!  @!@!!@!   
!!!       !!!       !!!!!:    !!!@!!!!  !!@!@!    
:!!       !!:       !!:       !!:  !!!  !!: :!!   
:!:        :!:      :!:       :!:  !:!  :!:  !:!  
 ::: :::   :: ::::   :: ::::  ::   :::  ::   :::  
 :: :: :  : :: : :  : :: ::    :   : :   :   : :  
""", 
      '\n')
try:

    location = input("[x] Please File Location => ")
    
    if not location.endswith('txt'):
        print("please give the extension as txt")
        
    for r in location:
        rep = r.replace("/", "\\")
        
    file = open(location)
    read = file.read()
    print("\n")
    clear = input("[+] Which character do you want to clear? => ")
    print("\n")
    save = input("[+] Specify where to save the file : ")
    output = open(save, "w", encoding="utf-8")

    for i in read.split():
        print(i.strip(clear), end="\n", file=output)

    print("\n", f"[+] File: {save} location saved", sep="")
    
except FileNotFoundError:
    print("File Path İs Wrong !")
