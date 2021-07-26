letter = 'a'
length = 5
for i in range(length + 1):
    print(letter * i)

for i in range(length - 1, 0, -1):
    print(letter * i)

length = 8
letter = 'b'
for i in range(length + 1):
    print(' ' * (length - i),end='')
    print(letter * i)

for i in range(length - 1, 0 , - 1):
    print(' ' * (length - i),end='')
    print(letter * i)

#going through alpahbet
#my_char = ord(letter)
#letter = chr(my_char + i)