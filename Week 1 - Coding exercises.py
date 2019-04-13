#Even or odd number

def even_or_odd(number):
    if number % 2 == 0:
        print("odd number")
    else:
        print("even number")
        
#Square of a number

def square_num(number):
    print(number**2)


#Fahrenheit to Celsius

def far_to_cel(number):
    print((number-32)/(9/5))

even_or_odd(4)
square_num(3)
far_to_cel(80)



#Return the largest number

def list_of_num (Numbers):
    
    result = Numbers[0]
    
    for number in Numbers:
        if number > result:
          result = number  
    
    print(result)
    
list_of_num([1,23,2,3,8,6])


#Palindrome

palindrome=input("Enter string to know if its a palindrome: ")
if(palindrome==palindrome[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")
 
 
#Vowels

vowel = ['a', 'e', 'i', 'o', 'u','y']
string = input("Enter string to know the number of vowels: ")
count = 0
for letter in string:
    if letter in vowel:
        count += 1
print("This string has",count,"vowels")