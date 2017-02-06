# python version of wc

filename = raw_input("FileName: ")
lines = 0
characters = 0
words = 0
wordSet = set()
with open(filename, 'r') as f:
    for line in f:
        lines += 1
        temp = line.split()
        wordSet.update(temp)
        words += len(temp)
        characters += len(line)

print "Lines: {}".format(lines)
print "Characters: {}".format(characters)
print "Words: {}".format(words)
print "Different Words: {}".format(len(wordSet))