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


# importing python random module to use random numbers and strings
import random

# function for getting names randomly when it is called
def get_random_names():
    f_names = ['Misbah', 'Rahul', 'Shahin', 'Kadir', 'Robiul', 'Mukesh', 'Zayed', 'Miftah', 'Nadir', 'Ruhit']
    random.shuffle(f_names)
    #print(f_names)

    l_name = ['Ahmed', 'Kabir', 'Gandi', 'Rahman', 'Khan', 'Uddin', 'Ambani', 'Karim']
    random.shuffle(l_name)
    #print(l_name)

    return f_names[1] + ' ' + l_name[-1]


# function for getting addresses randomly when it is called
def get_random_address():
    address1 = ['B/11', 'A/12', 'Level-4', 'Level-2', 'Street no: 05', 'Down Street', 'f/22', 'Down Town', 'Mountain Veiw']
    random.shuffle(address1)

    address2 = ['Dhanmondi', 'Gulshan', 'Bashundhara', 'Lusiana', 'Sylhet', 'Hacker Way', 'Clickbet', 'Griffindor', 'Ravinclaw']
    random.shuffle(address2)

    address3 = ['Dhaka', 'Bangladesh', 'Los Angeles', 'Harvard', 'Chattogram', 'India', 'Mumbai', 'Uttar Pradesh', 'Assam']
    random.shuffle(address3)

    return f'{address1[1]}, {address2[4]}, {address3[-1]}'


# function for getting phone numbers randomly when it is called
def get_random_phones():

    country_code = ['+880', '+971', '+1', '+44', '+977', '+47', '+41', '+33', '+11']
    random.shuffle(country_code)
    
    phone_preffix = ['11', '12' '13', '14', '15', '16', '17', '18', '19']
    random.shuffle(phone_preffix)

    phone_suffix = ''

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    for i in range(len(numbers)-2):
        phone_suffix += str(numbers[i])

    return f'{country_code[-1]} {phone_preffix[0]}{phone_suffix}'


# function for generating random email addresses
def get_random_email(name):
    email_preffix = name.lower().replace(" ", "")

    email_suffixes = ['@yahoo.com', '@gmail.com', '@outlook.com', '@hbr.org', '@info.me', '@programmer.com', '@engineer.com', '@int.com.bd', '@sure.com.in']
    random.shuffle(email_suffixes)

    return f'{email_preffix}{email_suffixes}'



#main program

number_of_info = int(input("How many info do you want? "))

for i in range(number_of_info):
    name = get_random_names()
    address = get_random_address()
    phone = get_random_phones()
    email = get_random_email(name)

    print(f'\n----- Information {i+1} -----\n\nName: {name} \nAddress: {address} \nPhone: {phone}\nEmail: {email}')
