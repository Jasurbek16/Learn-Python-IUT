""" Variable Naming Rules:
1. Must start with a letter or underscore (_)
2. Can only contain letters, digits, and underscores
3. Cannot be a reserved keyword in Python

NOTE: Variable names are case-sensitive. It means that "name" and "Name" are two different variables.
"""

## printing reserved keywords in Python
import keyword
print(keyword.kwlist) 

""" Conventions
1. snake_case for variables and functions
2. UPPERCASE for constants
3. PascalCase for classes
4. camelCase can be used but not recommended in Python
"""

my_func = 1
MAX_SIZE = 4
MyClass = 2
myVar = 3

""" Multiline Comments: 
Use triple double quotes, but that is better for docstrings. For multiline comments, use # for each line.
"""

course_name = "Introduction to IT"
full_name = "Jasurbek Mamurov"
custom_message = 'Hi Mark, I\'m interested in the "TOP-10" vscode extensions.' # "\" is an escape character, it is used to escape the next character in the string.

custom_multiline_message = '''Hi Elon,
I am really into applying for the "SpaceX" internship program.
I would like to know if you have any tips for me to get selected.
Thanks!'''

print(f'Big message:{custom_multiline_message}\n\nCordially,\n{full_name.upper()}\nLecturer\n{course_name}') # using f-string to format the string.
print("\nLength of full name: " + str(len(full_name))) # you need to convert the length (integer) to string before concatenating it with other strings.
print(type(len(full_name))) # checking the type of what's returned by len() function.
print("\n" + "Custom message: " + custom_message)

print("Name in custom message: " + custom_message[3:7]) # slicing the string to get a substring from index 3 to 6 (7 is not included - 3 is inclusive and 7 is exclusive).
print("Interesting part in custom message: " + custom_message[31:]) # slicing the string to get a substring from index 31 to the end of the string.

print(course_name.lower())
print(course_name.count("I")) # count() method counts the number of occurrences of a substring in a string.
print(course_name.find("IT")) # find() method returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
print(course_name.find("Physics")) # returns -1 because "Physics" is not found in the string.

course_name.replace("Introduction to IT", "Physics") # the replace() method returns a new string with the replacements made, but it does not change the original string.
print(course_name)

other_course_name = course_name.replace("Introduction to IT", "Physics") # so, we are assigning the updated string to a new variable.
print(other_course_name)

available_courses = "{}, {}".format(course_name, other_course_name) # it is also possible to use the format() method to format strings (instead of f-strings)
print(available_courses)

print(dir(full_name)) # dir() function returns a list of all the attributes and methods of an object (string in this case).
print(help(str)) # we are using the help() function to get the documentation of the str - string (class) data type.
print(help(str.lower)) # we are using the help() function to get the documentation of the str.lower - lower() method of string (class) data type.

###
### stuff below will be covered in the lab session-4
###

# num_1 = 10
# pi_in_math = 3.14

# print(type(num_1))
# print(type(pi_in_math))

### Arithmetic operations
## 5 + 2 
## 5 - 2
## 5 * 2
## 5 / 2
## 5 // 2
## 5 ** 2
## 5 % 2

# print(5 * (2 + 1))

# print(5 % 2)
# print(6 % 2)
# print(7 % 2)
# print(8 % 2)
# print(9 % 2)

# num_1 = 1 + num_1
# num_1 += 1
# num_1 -= 1

# negative_num = -5
# print(abs(negative_num))
# print(round(pi_in_math))
# print(round(pi_in_math, 1))

### Comparisions
## 5 == 2 
## 5 != 2
## 5 > 2
## 5 < 2
## 5 >= 2
## 5 <= 2

# number_1 = "5"
# number_2 = "2"
# print(number_1 + number_2)

# number_1 = int("5")
# number_2 = int("2")
# print(number_1 + number_2)

# available_courses = ["Introduction to IT", "Physics", "Mathematics", "Chemistry"]
# print(available_courses)
# print(available_courses[0])
# print(available_courses[1:])
# print(available_courses[-1])
# print(available_courses[4])

# available_courses.append("Biology")
# print(available_courses)

# available_courses.insert(0, "English")
# print(available_courses)

# course_list_2 = ["History", "Geography"]
# available_courses.insert(0, course_list_2)
# available_courses.extend(course_list_2)