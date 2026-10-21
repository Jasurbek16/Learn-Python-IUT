"""Inroduction to lists"""

# it_courses = ['Introduction to Python', 'Data Structures', 'Algorithms', 'Web Development', 'Machine Learning']
# print(it_courses[2:])
# print(it_courses[-2])

""".append() is used to add an item to the end of the list"""
# it_courses.append("Database Management") 
# print(it_courses)

""".insert() is used to add an item at a specific index in the list"""
# it_courses.insert(1, "AI")
# print(it_courses)

# art_courses = ['Digital Painting', 'Sculpture', 'Photography']

"""difference between list's .insert() and .extend() methods"""
# it_courses.insert(0, art_courses)
# it_courses.extend(art_courses)

""".remove() is used to remove some specific item from the list"""
# it_courses.remove('Algorithms')
# print(it_courses)

""".pop() is used to remove an item from the end of the list, or at a specific index if provided. It also returns the removed item, so you can assign it to a variable."""
# it_courses.pop()
# course_name = it_courses.pop()

# print(it_courses)
# print(course_name)

"""sorting elements in an ascending order (in an alphabetical order for strings) by default"""
# it_courses.sort()
# print(it_courses)

"""sorting elements in a descending order"""
# nums = [5, 2, 9, 1, 7]
# nums.sort(reverse=True)
# print(nums)
 

"""sorted() function returns a new sorted list without modifying the original list"""
# sorted_nums = sorted(nums)
# print(nums)
# print(sorted_nums)

# print(sum(nums))

"""getting an index of an element"""
# index_of_a_course = art_courses.index('Sculpture')
# print(index_of_a_course)

"""checking whether some element is in a list"""
# print('Sculpture' in art_courses)

"""'if statement' and 'for loop' can be used with lists but we will learn about them in detail in some other lab-class"""
# if 'Sculpture' in art_courses:
#     print('Sculpture is in the list of art courses.')

# for index, course in enumerate(it_courses):
#     print(index, course)

"""joining a list of strings into a single string and splitting a string into a list of strings"""
# print(it_courses)
# list_to_string = ", ".join(it_courses)
# print(list_to_string)

# print(list_to_string)
# string_to_list = list_to_string.split(", ")
# print(string_to_list)

"""lists are mutable, tuples are immutable, and sets are unordered collections of unique elements. 
This means that you can change the contents of a list, but you cannot change the contents of a tuple. 
Sets do not allow duplicate elements and do not maintain any specific order."""
# list_1 = [1, 2, 3]
# list_2 = list_1
# list_2[0] = 22
# print(list_1)
# print(list_2)

# tuple_1 = (1, 2, 3)
# tuple_2 = tuple_1
# tuple_2[0] = 22 
# print(tuple_1)
# print(tuple_2)

"""operations on sets: intersection, union, difference"""
# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4, 5, 6, 7, 8, 9}
# print(set_1.intersection(set_1))
# print(set_1.union(set_2))
# print(set_1.difference(set_2))