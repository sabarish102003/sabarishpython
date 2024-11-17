import time

def even(num:int):
    if num % 2 == 0 :
        print(f"{num} is even")
# even(4)

def vowel(char:str):
    if char in "aeiouAEIOU":
        print(f"{char} is vowel")

# vowel("b")

def single_value(value:int|float|complex|bool):
    list1 = [int,float,complex,bool]
    if type(value) in list1:
        print(f"{value} is single value datatype")

# single_value(True)

def upper(word:str):
    first_char = word[0]
    if first_char.isupper():
        print(f"{word} is starting with upper case")

#upper("sabarish")

def positive_number(num:int=0):
    if num >=  0 :
        print(f"{num} is positive integer")

# positive_number(1)

def divisor(num:int):
    if num % 5 == 0 and num % 3 == 0:
        print(f"{num} is divisible of by 5 and 3")

# divisor(9)

def lenofnumber(num:int):
    length = len(str(num))
    # if length == 3:
    if 100 >= num <= 1000 or -100<= num >=-999:
        print(f"{num} is three digit nubmer")

# lenofnumber(-678)

def subset(set1:set,set2:set):
    if set2.issubset(set1):
        print(f"{set2} is subset of {set1}")

# subset({1,2,3,4,5},{3,4})

def palindrom(word:str):
    temp = word[::-1]
    if word == temp:
        print(f"{word} is palindrom")

# palindrom("apple")

def positive_negative(num:int):
    if num >= 0 :
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")

# positive_negative(-2)

def special(char:str):
    if char.isalnum():
        print(f"{char} is not special character")
    else:
        print(f"{char} is special character ")

# special("A")

def square_odd(num:int):
    if num % 2 == 0:
        print(f"this is even so the square of {num} is {num**2}")
    else:
        print(f"this is odd so the cude of {num} is {num**3}")

# square_odd(4)

import keyword

def key_word(word:str):

    keywords = keyword.kwlist 
    if word in keywords:
        print(f"{word} is keyword")
    else:
        print(f"{word} is not keyword")

# key_word("None")

def lenofcollection(collection:list|tuple|set):
    length = len(collection)
    if length < 5:
        print(f"this collection is length is less then 5")
    else:
        print(f"this collection is length is more then 5")

# lenofcollection([1,2,3,4,5,6,7,4,5,6,7,5])

def datatypevalidation(data):
    if type(data) in (int,float,complex,bool):
        print(f"{data} is single value datatype")
    else:
        print(f"{data} is collection datatype")

# datatypevalidation([1,2,3,4])

def vowel_or_consonent(char:str):
    if char in "AEIUOaeiou":
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonent")

# vowel_or_consonent("d")

def displaynumber(nums:int):
    for num in range(nums+1):
        print(num)
        time.sleep(.5)
        num += 1

# displaynumber(10)

def result(mark:int):
    if mark >=90:
        print("your grade is O")
    elif mark >=80:
        print("your grade is A")
    elif mark >=70:
        print("your grade is B")
    elif mark >=60:
        print("your grade is c")
    elif mark >=50:
        print("you are passed")
    else:
        print("your are Failed")

# result(5)

def type_of_character(char):
    if type(char) == str:
        if char.isupper():
            print("this is in uppercase")
        elif char.islower():
            print("this is in lowercase")
        else:
            print("this is special character")
    else:
        print("this is interger")

# type_of_character("a")

def type_of_set(set1:set,set2:set):
    if set1 > set2:
        print(f"{set1} is superset of {set2}")
    elif set1 < set2:
        print(f"{set1} is subset of {set2}")
    elif set2 < set1:
        print(f"{set2} is subset of {set1}")
    else:
        print("disjoint sets")

set2= {1,2,3,4,5}
set1 = {7,7,6}
# type_of_set(set1,set2)

def relation(num1:int,num2:int):
    if num1 > num2:
        print(f"{num1} is greater then {num2}")
    elif num1 < num2:
        print(f"{num2} is greater then {num1}")
    else:
        print(f"{num1} is equal to {num2}")

# relation(7,7)

def digitsofnum(num:int):
    if -9>=num<=9:
        print(f"{num} is single digit")
    elif 10>=num<=99 or -10<=num>=-99:
        print(f"{num} is two digit ")
    elif 


    
  



    

    
    
        

        
        

        






















    