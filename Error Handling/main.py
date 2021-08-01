"""
Error Handling:

Function from "If" statements HW
"""

number_1 = 6
number_2 = 5
str_number = "5"

def comapre(param_1,param_2,param_3):
    try:
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
    except ValueError:
        print('ValueError: Only numbers are allowed!')
    except TypeError:
        print('Type error: Please enter only numbers or there is a missing argument!')
    except Exception:
        print('Exception: Only numbers are allowed!')
    finally:
        pass
        #print('Finally')


print('Result:',comapre(1,2,3))
print('Result:',comapre('a','b','c'))
print('Result:',comapre(True,False,False))
print('Result:',comapre('5','2','5'))
print('Result:',comapre(True,{1:'a',2:'b',3:'c'},5))
print('Result:',comapre('2','5.456','5.456'))
print('Result:',comapre(1,2,['a','b']))
print('Result:',comapre('5',False,'5'))
print('Result:',comapre({5,5,5},'','5'))
print('Result:',comapre('','',''))
