# python3
# 𝕰𝖋𝖑𝖔𝖚𝖉

try:

    print('\n')
    location = input('Please File Location => ')
    file = open(location)
    read = file.read()
    print('\n')
    clear = input('[+] Which character do you want to clear? => ')
    print('\n')
    save = input('[+] Specify where to save the file :')
    output = open(save, 'w', encoding='utf-8')

    for i in read.split():
        print(i.strip(clear), end='\n', file=output)


except FileNotFoundError:
    print('File Path İs Wrong !')

