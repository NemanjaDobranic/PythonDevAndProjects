number_1 = 6
number_2 = 5
str_number = "5"

def comapreThreeParam(param_1,param_2,param_3):
    value_1 = int(param_1) 
    value_2 = int(param_2)
    value_3 = int(param_3)

    if value_1 == value_2:
        return True
    elif value_1 == value_3:
        return True
    elif value_2 == value_3:
        return True
    else:
        return False

result = str(comapreThreeParam(number_1,number_2,str_number))

print('Equality between any of numbers ' + str(number_1) + ', '\
    + str(number_2) + ' and '+ str(str_number) + ' is : ' + result)

#another examples
print(comapreThreeParam(15,6,-5))
print(comapreThreeParam(2,"-10",-10))
