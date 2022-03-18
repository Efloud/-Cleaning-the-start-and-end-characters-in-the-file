####

# # #
# Clearing Character
# # #

####

print('\n')
location = input('Please File Location => ')
file = open(location)
read = file.read()
print('\n')
clear = input('Which character do you want to clear? => ')

for i in read.split():
    print(i.strip(clear), end='\n')
file.close()
