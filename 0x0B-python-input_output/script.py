with open('test.txt', mode='a') as my_file:
    text = my_file.write('hey, it\' me!')
    print(text)