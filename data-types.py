### important: variable naming rules
## 1. must start with a letter or underscore (_)
## 2. can only contain letters, digits, and underscores
## 3. cannot be a reserved keyword in Python

### printing reserved keywords in Python
# import keyword
# print(keyword.kwlist)

### note: variable names are case-sensitive. it means that "name" and "Name" are two different variables.

### conventions
## 1. snake_case for variables and functions
## 2. UPPERCASE for constants
## 3. PascalCase for classes
## 4. camelCase can be used but not recommended in Python
# my_func = 1
# MAX_SIZE = 4
# MyClass = 2
# myVar = 3

### multiline comments: use triple quotes, but that is better for docstrings. For multiline comments, use # for each line.

"""Hello. This must be visible inside my new repo."""

# course_name = "Introduction to IT"
# full_name = "Jasurbek Mamurov"
# custom_message = 'Hi Mark, I\'m interested in the "TOP-10" vscode extensions.'

# custom_multiline_message = '''Hi Elon,
# I am really into applying for the "SpaceX" internship program.
# I would like to know if you have any tips for me to get selected.
# Thanks!'''

# print(f'Big message:{custom_multiline_message}\n\nCordially,\n{full_name.upper()}\nLecturer\n{course_name}')
# print("\nLength of full name: " + str(len(full_name)))
# print("\n" + "Custom message: " + custom_message)

# print("Name in custom message: " + custom_message[3:7])
# print("Interesting part in custom message: " + custom_message[31:])

# print(course_name.lower())
# print(course_name.count("I"))
# print(course_name.find("IT"))
# print(course_name.find("Physics"))

# course_name.replace("Introduction to IT", "Physics")
# print(course_name)

# other_course_name = course_name.replace("Introduction to IT", "Physics")
# print(other_course_name)

# available_courses = "{}, {}".format(course_name, other_course_name)
# print(available_courses)

# print(dir(full_name))
# print(help(int))
# print(help(str.lower))

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