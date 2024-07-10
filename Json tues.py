#Stores and exchange data
#Data types inside JSON,It uses a number,String,Object, Boolean and Array

#A code to convert JSON data to python objects

# import json                                          #import JSON package
# Json_Object = '{"Name":"David","Class":"I","Age":6}' #line 7 Json string
# python_Object = json.loads(Json_Object)              #convert Json string into python objects
# print("\nJSON data:")                                
# print("\nJSON data:",python_Object)
# print("\nName:",python_Object["Name"])                 
# print("Class:",python_Object["Class"])
# print("\Age:",python_Object["Age"])


#a code to convert Python data to Json data type
# import json

# python_Object = {"Name":"David","Class":"I","Age":6}
# Json_Object = json.dumps(python_Object)  

# print(type(Json_Object))
# print(python_Object)

#Python objects into JSON strings
# import json
# xp = {"Name":"Romeo","Surname":"Sebola","Age":"19"}
# courses_lp = ["Com Sci","Data science","IT","Statistics"]
# yearp = 2024


# xj = json.dumps(xp)
# courses_lj = json.dumps(courses_lp)
# yearj = json.dumps(yearp)

# print("fROM PYTHON DICTIONARY ",xj)
# print("fROM PYTHON LIST ",courses_lj)
# print("fROM PYTHON INT ",yearj)

#Python dictionary objects 
 
#a code to convert json data encoded data into python object

# import json
# xj = '{"Name":"Romeo","Surname":"Sebola","Age":"19"}'
# courses_lj = '["Com Sci","Data science","IT","Statistics"]'
# yearj = '2024'
# intj = '1234556789'
# floatj = '234.55'
# bool_ = 'true'

# python_dict = json.loads(xj)
# python_list = json.loads(courses_lj)
# python_int = json.loads(yearj)
# python_float = json.loads(floatj)
# python_bool = json.loads(bool_)

# print("Python dictionary:",python_dict)
# print("python_list:",python_list)
# print("Python Int...:",python_int)
# print("Python float:",python_float)
# print("Python Bool:",python_bool)


# print(type(python_bool))

#A document that is validated or checked,The schema of a document has a description
# A code to check if an object is a complex number

# import json
# def encode_complex(object):
#     if isinstance(object, complex):
#         return [object.real,object.imag]

#     raise TypeError(repr(object) + " is not json serialized")

# complex_obj = json.dumps(2+3j, default = encode_complex) 
# print(complex_obj)

#Arrays
#A code that will display array of 5 integers
# from array import*
# array_num = array('i',[2,3,4,6,0])


# print("Access first 3 items individually")
# print(array_num[2])
# print(array_num[3])
# print(array_num[4])
# #A code that is going to append a new a item to the end of the array

# array_num.append(11)
# print(array_num[5])

#Write an array


#Classes
#Write a code that is going to import a built in array module and display ... module
# import array
# for name in array.__dict__
# print(name)

#python function that studen id student name class

# def student(student_id,student_name,student_class):


#Hashlib is a module in python
#It can securely transform data into a fixed size sequence of bytes
#sha-256 an encryption method used in cyber security
#Unicode transformation method 8 bits(utf-8)
#Converts bytes to string object "UTF-8"

#re- regular expressions or regex, it works with text data, re has all the characters needed for password

#a function to take a password as input and return list of common characters

# def get_password_variants(password):
#     pass_variants = []
#     substitutions = {
#         'a': ['@', '4', 'A'],
#         'e': ['3', 'E'],
#         'i': ['1', '!', 'I'],
#         'o': ['0', 'O'],
#         's': ['$', '5', 'S'],
#         't': ['7', 'T'],
#         'z': ['2', 'Z']
#     }
    
#     for i in range(len(password)):
#         if password[i] in substitutions:
#             for sub in substitutions[password[i]]:
#                 pass_variant = password[:i] + sub + password[i+1:]
#                 pass_variants.append(pass_variant)
    
#     pass_variants.append(password + '!')
#     pass_variants.append(password + '123')
#     pass_variants.append(password + '@')
#     pass_variants.append(password + '#')
#     pass_variants.append(password + '$')
#     pass_variants.append(password + '%')
#     pass_variants.append(password + '&')
#     pass_variants.append(password + '*')
#     pass_variants.append(password + '-')
#     pass_variants.append(password + '_')
#     pass_variants.append(password + '=')
#     pass_variants.append(password + '+')    
#     return pass_variants
?


#Crete dqlite database
#a code for sqlite connect to a database
#print the the version

import sqlite3

try:
    sq_connection = sqlite3.connect('connect.db')
except:
    print(sq_connection)