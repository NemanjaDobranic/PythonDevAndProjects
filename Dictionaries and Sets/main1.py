#pylint - Linting highlights syntactical and stylistic problems in your Python source code (Problems)


#Sets 
# - they do not preserve elements order
# - Used only when want to know that there is a certain element 
# but it is not important if it repeats many time - saves memory resources
# 
"""
CountryList = []
Sets = {}

for i in range (5):
    country = input('Enter a country: ')
    CountryList.append(country)

Sets = set(CountryList)

print(CountryList)
print(Sets)
"""

#All of Python's immutable built-in objects are hashable (can be used as keys), 
# while no mutable containers (such as lists or dictionaries) are
#So there is error
"""
Sets = {"sun",123,45.65,[1,'1']}
print(Sets)
"""
""""
Sets = {"sun",123,45.65}
print(Sets)
"""

#Dictionaries
#- they do not preserve elements order
#- key:value, key is hashable
#- values() is an inbuilt method in Python programming language 
# that returns a list of all the values available in a given dictionary.

"""
BlackShoes = {42:3,38:0,39:1,41:2,40:4}

while True:
    shoeSize = int(input('Enter a shoe size: '))
    if shoeSize < 0:
        break
    elif shoeSize not in BlackShoes:
        print('Shoe size ' + str(shoeSize) + ' is not available')
        continue        #skip rest of code
    if BlackShoes[shoeSize] > 0:     #shoeSize is key
        BlackShoes[shoeSize] -=1
    else:
        print('Shoe size ' + str(shoeSize) + ' is not in stock')

    print(BlackShoes)
"""