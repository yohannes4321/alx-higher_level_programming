a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if key==a_dictionary.keys():
            a_dictionary[key]=value
    
    a_dictionary[key]=value
    return sorted(a_dictionary.items())
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print(new_dict)
print('-------------------------')
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print(new_dict)
