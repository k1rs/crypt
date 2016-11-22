import string

dictionary = set(open('words.txt','r').read().lower().split())
max_len = max(map(len, dictionary))

file = open("input.txt", 'r')

str = file.readline()
str = str.rstrip('\n').decode("hex") #Delete \n in raw data and decode HEX
str_xored = ""

string_printed_key = 0

print "XOR decoded combinations: "

letters = list(string.ascii_letters)
for i in letters:
    for t in str:
        str_xored = str_xored + chr(ord(t)^ord(i))
    str_xored = str_xored.lower() 

    c = 0 #char price of the word

    for t in str_xored:
        if t == 'e':
            c = c + 12.7
        if t == 't':
            c = c + 9.1
        if t == 'a':
            c = c + 8.2
        if t == 'o':
            c = c + 7.5
        if t == 'i':
            c = c + 7.0
        if t == 'n':
            c = c + 6.7
        if t == 's':
            c = c + 6.3
        if t == 'h':
            c = c + 6.1
        if t == 'r':
            c = c + 6.0
        if t == 'd':
            c = c + 4.3
        if t == 'l':
            c = c + 4.0
        if t == 'u':
            c = c + 2.8
        if t == 'c':
            c = c + 2.8
        if t == 'm':
            c = c + 2.4
        if t == 'w':
            c = c + 2.4
        if t == 'f':
            c = c + 2.2
        if t == 'y':
            c = c + 2.0
        if t == 'g':
            c = c + 2.0
        if t == 'p':
            c = c + 1.9
        if t == 'b':
            c = c + 1.5
        if t == 'v':
            c = c + 1.0
        if t == 'k':
            c = c + 0.8
        if t == 'x':
            c = c + 0.2
        if t == 'j':
            c = c + 0.2
        if t == 'q':
            c = c + 0.1
        if t == 'z':
            c = c + 0.1
    if c > len(str_xored)*4:
        for i in xrange(len(str_xored)): #for each possible starting position in the corpus
            chunk = str_xored[i:i+max_len+1] #chunk that is the size of the longest word
            for j in xrange(1,len(chunk)+1): #loop to check each possible subchunk
                    word = chunk[:j] #subchunk
                    if word in dictionary: #constant time hash lookup if it's in dictionary
                        if string_printed_key == 0:
                            print str_xored #add to set of words
                            string_printed_key = 1
    c = 0
    str_xored = ""
    string_printed_key = 0