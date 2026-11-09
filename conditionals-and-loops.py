university = {'name': 'Inha University', 'location': 'Incheon', 'established': 1954, 'students': 15000, 'students_coming_from': ['Uzbekistan', 'China', 'Vietnam', 'Philippines']}
# university['name'] = 'Westminster University'

# print(university['name'])
# university['president'] = 'Dr. Hello'
# print(university)

# print(university)
# university.update({'name': 'West', 'president': 'Dr. Hello', 'phone': '12-34-56'})
# print(university)

# location = university.pop('location')
# print(location)
# print(university)

# del university['students_coming_from']
# print(university)

# print(university.keys())
# print(university.values())
# print(university.items())

# for key, value in university.items():
#     print(key, value)

###

# language = 'PHP'

# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# else:
#     print('Not found!')

# name = 'Admin'
# logged_in = False
# names = ['Ertugrul', 'Komronbek', 'Sultanbek', 'Amaliya']

# if name == 'Admin' or logged_in:
#     print('Welcome Admin!)')
# else:
#     print('Access denied!!!')

# if not 'Aziza' in names:
#     print('She\'s found!')
# else:
#     print("Where's she?")

# print('Aziza' in names)
# print(not 'Aziza' in names)
# print('Aziza' not in names)

###
names = ['Ertugrul', 'Komronbek', 'Sultanbek', 'Amaliya']
nums = [1, 2, 3]

# for loop
# for name in names:
#     print(name)

for name in names:
    for num in nums:
        print(num, name)


# while loop
