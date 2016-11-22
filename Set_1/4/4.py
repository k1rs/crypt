import string
dictionary = set(open('words.txt','r').read().lower().split())
max_len = max(map(len, dictionary))
letters = list(string.ascii_letters + string.digits) #add numbers

string_counter = 1

with open('input.txt') as file:
    for line in file:
        string_header_printed = 0
        str = line.rstrip('\n').decode("hex")

        for i in letters:
            str_xored = ""
            xor_variation_printed = 0
            for t in str:
                str_xored = str_xored + chr(ord(t)^ord(i))
            str_xored = str_xored.lower() 

            c = 0 #char price of the string

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
                eng_word_in_string_counter = 0
                for y in xrange(len(str_xored)): #for each possible starting position in the corpus
                    chunk = str_xored[y:y+max_len+1] #chunk that is the size of the longest word
                    for j in xrange(4,len(chunk)+1): #loop to check each possible subchunk
                            word = chunk[:j] #subchunk
                            if word in dictionary: #constant time hash lookup if it's in dictionary
                                eng_word_in_string_counter = eng_word_in_string_counter + 1
                                if eng_word_in_string_counter > 3: #check for TRUE eng message
                                    if string_header_printed == 0:                                
                                        print "Possible decrypted messages in string #%d:\n" %(string_counter)
                                        string_header_printed = 1
                                    if xor_variation_printed == 0:
                                        print " " + chr(254) + " " + str_xored

                                        xor_variation_printed = 1
                eng_word_in_string_counter = 0
            xor_variation_printed = 0
        string_header_printed = 0
        string_counter = string_counter + 1