file = open("input.txt", 'r') #Open file with source code

hex_string = file.readline()
print "HEX encoded string: " + hex_string
base64_string = hex_string.decode("hex").encode("base64") #Decode HEX and instant encode to base64
print "Base64 Encoded string: " + base64_string
print "A funny secret message: " + base64_string.decode("base64")