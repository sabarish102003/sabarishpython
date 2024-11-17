def remove_vowels(word):
    vowels  = 'aeiouAEIOU'
    new_word = ''
    for char in word:
        if char not in vowels:
            new_word += char
    print(new_word)
    

# def factorial(collection : list|tuple|set):
#     new_collection = []
#     for element in collection:
        
#         if type(element) == str:
#             remove_vowels(element)
#         else:
#             new_collection.append(element)


# factorial(['sabarish','baranish',9024])


list1 = ["sab","bar"]
for element in list1:
    length = 1
    for length in range(len(element)):
        if length <= len(element)-1:
            length = length * length - 1
    print(length)
            





                

                 