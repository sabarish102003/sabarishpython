def max_factorial(collection : list | tuple | set):
    new_collection = []
    vowels = "aeiouAEIOU"
    
    for element in collection:
        new_element = ""
        if type(element) == str :
            for char in element:
                if char not in vowels:
                    new_element += char
            new_collection.append(new_element)
        else:
            new_collection.append(element)
    print(new_collection)

max_factorial(['sabarish','baranish',9024])


