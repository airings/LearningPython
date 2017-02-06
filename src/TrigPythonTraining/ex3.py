# Pig Latin

# get a sentence from the user
# and translate each word
# and then print the resulting translation
# on a single line

while(True):
    inputStrs = raw_input("Please input: ").strip().lower()
    resl = []
    for word in inputStrs.split():
        if word[0] in 'aeiou':
            resl.append(word + 'way')
        else:
            resl.append(word[1:] + word[0] + 'ay')
    print ' '.join(resl)