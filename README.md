# CEB1250_repo

'''Even or odd number''' 

def even_or_odd(number):
   
   if number % 2 == 0:
        print("odd number")
    else:
        print("even number")
        
        
'''Square of a number'''
def square_num(number):
    print(number**2)

def far_to_cel(number):
    print((number-32)/(9/5))

even_or_odd(4)
square_num(3)
far_to_cel(80)


'''Create a method (function) that takes a list of numbers. Return the largest number in the list.'''

def list_of_num (Numbers):
    
    result = Numbers[0]
    
    for number in Numbers:
        if number > result:
          result = number  
    
    print(result)
    
list_of_num([1,2,3,4125,6])
