filename = input("whats the file name? ")
content = input("Enter content you want to add")

with open(filename,'w') as file:
    file.write(content)

file_open = input('enter y or n')

if file_open in ['y','n']:
    if file_open == 'y':
        with open(filename,'r') as file:
            print(file.read())
    else:
        print('closed and saved')