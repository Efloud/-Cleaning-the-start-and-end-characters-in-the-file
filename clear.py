# python 3
####

# # #
# Clearing Character
# # #

####

try:
    print('\n')
    location = input('Please File Location => ')
    file = open(location)
    read = file.read()
    print('\n')
    clear = input('Which character do you want to clear? => ')
    for i in read.split():
        print(i.strip(clear), end='\n')
except FileNotFoundError:
    print('File Path İs Wrong')
