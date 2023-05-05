'''
Program Description:
This is a program that generates fake user info generating their name, address, phones and emails randomly.
This is a hardcoded program that means the fake names, addresses, phones and emails are written in actual code.
This program just shuffles around the hardcoded information randomly.
This program will generate any number of information you want, so it will ask to input the number of info you want each time it runs.

Disclaimer:
This is just a practice program to get a crystal clear idea about the Python random module and how it works.
The codes must not be used in any illegal activity or by AI.
If it occurs, the writer of the program will not be responsible for this.
'''

import random


first_name = ['Misbah', 'Rafique', 'Rahed', 'Rakib', 'Sam', 'Geoffry', 'Hitter', 'Krish', 'Cooler', 'Ruhit', 'McCulum', 'Ravin', 'Rustom', 'Hayat', 'Rukhshana', 'Harris', 'Jonny', 'Rubina', 'Rose', 'Jack', 'Tiff', 'Saleha', 'Bushra', 'Kaderi', 'Salma', 'Sadia', 'Tutul', 'Stephine', 'Mosh', 'Rudela', 'Kafii', 'Ruhul']
last_name = ['Ahmed', 'Rahman', 'Kabir', 'Mitro', 'Naik', 'Altman', 'Clean', 'Islam', 'Hinton', 'Kunal', 'Sharma', 'Khan', 'Jadeja', 'Askar', 'Jeyy', 'Hamedani', 'Ali']
address1 = ['34 Hacker Way', 'Mountain Veiw', '3/11 Ashuliya', 'A/34 Gulshan', '5 - Street View', 'New Road', 'H-07 Hilton', 'Gryffindor', 'Harmoine', 'Slytherin', 'Hook - 05', 'Heague', 'Rust 09', 'Level - 09', 'Down Town', 'Downing Street']
address2 = ['Silicon Vally', 'LA', 'California', 'Dhaka', 'Chattogram', 'London', 'Cambridge', 'Oxford', 'Massatussetts', 'New Jersey', 'New York', 'Bay Area', 'West Mister', 'Mumbai', 'Bengaluru', 'Kerala']

number_of_info = int(input('How many info do you want? '))

for i in range(number_of_info):
    name = random.choice(first_name) + ' ' + random.choice(last_name)
    address = random.choice(address1) + ', ' + random.choice(address2)
    phone = str(random.randint(1000, 9999)) + '-' + str(random.randint(1000, 9999)) + '-' + str(random.randint(1000, 9999))
    email = name.replace(" ", "").lower() + '@gmail.com'

    print(f'\n---- Person {i+1} ----\n\nName: {name}\nAddress: {address}\nPhone: {phone}\nEmail: {email}')



