#This is a decoder mf
key = raw_input('Enter your KEY: ')
output_file = open("output.txt",'wb')#this is first shiet
with open("input.txt",'rb') as input_file:
    xor_counter = 0 #!
    while True:
        char = input_file.read(1)
        if char == "\r":
            continue
        if not char:
            break
        if xor_counter == len(key):
            xor_counter = 0
        print char + "  %d" %ord(char)
        print (chr(ord("I")^13)).encode("hex")
        print (chr(ord("C")^13)).encode("hex")
        print (chr(ord("E")^13)).encode("hex")
        print (chr(ord("I")^10)).encode("hex")
        print (chr(ord("C")^10)).encode("hex")
        print (chr(ord("E")^ord("l"))).encode("hex")
        output_file.write(chr(ord(char)^ord(key[xor_counter])).encode("hex"))
        xor_counter += 1
output_file.close()
input_file.close()
