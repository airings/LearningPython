# Pig Latin

while(True):
    inputStr = raw_input("Please input: ").strip()

    # if inputStr[0] in ('a','e','i','o','u'):
    if inputStr[0] in 'aeiou':
        print inputStr + 'way'
    else:
        print inputStr[1:] + inputStr[0] + 'ay'



