def get_all_lines(dirname):
    import os
    files = os.listdir(dirname)

    for file in os.listdir(dirname):
        try:
            for index, line in enumerate(open(file, 'r')):
                print "{}:{} {}".format(file, index, line)
        except IOError:
            print "Cannot open {}; ignoring".format(file)
            continue


get_all_lines(".")