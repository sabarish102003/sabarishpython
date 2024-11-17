def max_factroial():
    collection = eval(input("enter a collection:"))
    new_collection=[]
    vowel = ["a","A","E","e","I","i","o","O","U","u"]
    for element in collection:
        word = str(element)
        if type(element)==str:
                mod = element.replace(vowel,"")
                 
        new_collection.append( mod )
    print (new_collection)
                            
max_factroial()
            
