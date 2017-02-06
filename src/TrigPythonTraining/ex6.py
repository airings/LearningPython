
addressbook = []

while True:
    print addressbook
    command = raw_input("Please input command[q,a,l,f,w,r]: ")
    if command in 'qalfwr':
        if command == 'q': break
        elif command == 'a':
            contact = {}
            contact['GivenName'] = raw_input("Given Name: ")
            contact['FamilyName'] = raw_input("Family Name: ")
            contact['Phone'] = raw_input("Phone: ")
            contact['E-mail'] = raw_input("E-mail: ")
            addressbook.append(contact)

        elif command == 'l':
            for contact in addressbook:
                print contact
                print "{},{} phon {} email {}".format(contact['GivenName'],
                                                      contact['FamilyName'],
                                                      contact['Phone'],
                                                      contact['E-mail'])

        elif command == 'f':
            look_for = raw_input("Search Name: ")
            for contact in addressbook:
                if (look_for in contact['GivenName']  or
                    look_for in contact['FamilyName'] or
                    look_for in contact['E-mail']):
                    print "{},{} phon {} email {}".format(contact['GivenName'],
                                                          contact['FamilyName'],
                                                          contact['Phone'],
                                                          contact['E-mail'])
            else:
                print "Sorry! Don't find {}".format(look_for)

        elif command == 'w':
            with open("/tmp/addressbook.txt", 'w') as f:
                head = "GivenName,FamilyName,Phone,E-mail"
                f.write(head+'\n')
                for contact in addressbook:
                    line = []
                    for key in head.strip().split(","):
                        line.append(contact[key])
                    f.write(",".join(line)+'\n')

        else:
            with open("/tmp/addressbook.txt", 'U') as f:
                head = f.readline()
                addressbook = []
                for line in f:
                    contact = {}
                    ll = line.strip().split(',')
                    for index, key in enumerate(head.strip().split(",")):
                        contact[key] = ll[index]
                    addressbook.append(contact)

