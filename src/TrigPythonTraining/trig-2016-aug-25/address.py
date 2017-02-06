#!/usr/bin/env python

people = [ ]
filename = '/tmp/people'

while True:
    print people

    user_choice = raw_input("Enter command: ")

    if user_choice == 'q':
        break

    elif user_choice == 'a':
        new_person = {}
        for field in ['given_name', 'family_name', 'email', 'phone']:
            new_person[field] = raw_input("Enter {}: ".format(field))
        people.append(new_person)

        # metaprogramming


        # given_name = raw_input("Enter given name: ")
        # family_name = raw_input("Enter family name: ")
        # phone = raw_input("Enter phone: ")
        # email = raw_input("Enter email: ")

        # new_person = {'given_name': given_name,
        #               'family_name': family_name,
        #               'phone': phone,
        #               'email': email}
        # people.append(new_person)

    elif user_choice == 'w':
        with open(filename, 'w') as f:
            for person in people:
                f.write("{}\t{}\t{}\t{}\n".format(person['given_name'],
                                                  person['family_name'],
                                                  person['email'],
                                                  person['phone']))
                                                  
    elif user_choice == 'r':
        people = [ ]
        for line in open(filename):
            (given_name, family_name, phone,
             email) = line.strip().split('\t')
            new_person = {'given_name': given_name,
                          'family_name': family_name,
                          'phone': phone,
                          'email': email}
            people.append(new_person)

    elif user_choice == 'l':
        for person in people:
            print "{} {}, ph {}, email {}".format(person['given_name'],
                                                  person['family_name'],
                                                  person['phone'],
                                                  person['email'])
                                                     
    elif user_choice == 'f':
        look_for = raw_input("Enter search string: ")
        for person in people:
            if (look_for in person['given_name'] or
                look_for in person['family_name'] or
                look_for in person['email']):
                print "{} {}, ph {}, email {}".format(person['given_name'],
                                                      person['family_name'],
                                                      person['phone'],
                                                      person['email'])
                                                     

    else:
        print "I don't know how to {}".format(user_choice)

print "Bye!"        

# Each person:

# list of dicts

# - given name
# - family name
# - phone number
# - e-mail address

# User can enter a command by typing a letter (and then enter):

# - q: quits from the program
# - a: asks the user 4 questions, and uses the answers to add
#      someone to the address book
# - l: list everyone in the address book
# - f: ask for a search string, and show all people with
#      that string in their name (either one) or e-mail address

# If you feel up to it:
# - w: write information from address book to disk (overwriting)
# - r: read information from disk to address book (overwriting)
