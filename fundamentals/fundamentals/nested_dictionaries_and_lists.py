# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"

print(students)

sports_directory["soccer"][0] = "Andres"

print(sports_directory)

z[0]["y"] = 30

print(z)

# 2 Iterate Through a List of Dictionaries 

# def iterateDictionary(some_list):
#     for i in range(len(some_list)):
#         print(some_list[i])


def iterateDictionary(some_list):
    for i in some_list:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# print(iterateDictionary(students))

# print(students[0]["last_name"])


# 3 Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    # for i in range(len(some_list)):
    #     print(some_list[i][key_name])
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4 Iterate Through a Dictionary with List Values


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for val in some_dict[key]:
            print(val)



printInfo(dojo)























# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(some_dict):
#     for key, val in some_dict.items():
#         print(some_dict.items())
#         print(len(val), key.upper())
#         print(val)

# printInfo(dojo)


# LECTURE WAY OF DOING IT

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# # def printInfo(some_dict):
# #     for key in some_dict:
# #         print(f"{key} {some_dict[key]}")

# # printInfo(dojo)


# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for key in some_dict:
#         print(len(some_dict[key]), key.upper())
#         for val in some_dict[key]:
#             print(val)



# printInfo(dojo)
